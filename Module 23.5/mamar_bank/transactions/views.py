from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import redirect, get_object_or_404
from django.db.models import Sum
from django.contrib import messages
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, View
from datetime import datetime
from accounts.models import UserBankAccount
from .forms import (
    DepositForm,
    WithdrawForm,
    LoanRequestForm,
    MoneyTransferForm
)
from .models import Transaction
from .constants import (
    DEPOSIT,
    WITHDRAWAL,
    LOAN,
    LOAN_PAID,
    TRANSFER,
    RECEIVE
)

# Create your views here.

def send_transaction_email(user, subject, template, amount = 0, user2 = None):
    context = {
        'user': user,
        'amount': amount,
    }
    if user2:
        context.update({
            'user2' : user2,
        })

    message = render_to_string(template, context)
    send_email = EmailMultiAlternatives(subject, '', to=[user.email])
    send_email.attach_alternative(message, 'text/html')
    send_email.send()

class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    model = Transaction
    template_name = 'transactions/transaction_form.html'
    title = ''
    success_url = reverse_lazy('transaction_report')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account' : self.request.user.account # Pass the account to the form
        })
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title' : self.title
        })
        return context

class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = 'Deposit'
    
    def get_initial(self):
        initial = {'transaction_type' : DEPOSIT}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount
        account.save(
            update_fields = ['balance']
        )
        
        messages.success(self.request, f'{amount}$ was deposited to your account successfully')
        send_transaction_email(
                user = self.request.user,
                subject = "Deposite Message",
                amount = amount,
                template = "transactions/deposit_email.html"
            )
        
        return super().form_valid(form)
    
class WithdrawaMoneyView(TransactionCreateMixin):
    form_class = WithdrawForm
    title = 'Withdraw Money'
    
    def get_initial(self):
        initial = {'transaction_type' : WITHDRAWAL}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        total_bank_balance = UserBankAccount.objects.aggregate(Sum('balance'))['balance__sum'] or 0
        if total_bank_balance < amount:
            return HttpResponse("The bank is bankrupt. Withdrawal cannot be processed.")
        
        account = self.request.user.account
        account.balance -= amount
        account.save(
            update_fields = ['balance']
        )
        
        messages.success(self.request, f'Successfully withdrawn {amount}$ from your account')
        
        send_transaction_email(
                user = self.request.user,
                subject = "Withdrawal Message",
                amount = amount,
                template = "transactions/withdrawal_email.html"
            )
        
        return super().form_valid(form)
    
class LoanRequestView(TransactionCreateMixin):
    form_class = LoanRequestForm
    title = 'Request For Loan'
    
    def get_initial(self):
        initial = {'transaction_type' : LOAN}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        current_loan_count = Transaction.objects.filter(account= self.request.user.account, transaction_type=LOAN, loan_approve=True).count()
        
        if current_loan_count >= 3:
            return HttpResponse("You have crossed your limits")
        
        messages.success(self.request, f'Loan request for amount {amount}$ has been successfully sent to admin')
        
        send_transaction_email(
                user = self.request.user,
                subject = "Loan Request Message",
                amount = amount,
                template = "transactions/loan_request_email.html"
            )
        
        return super().form_valid(form)

class TransactionReportView(ListView):
    template_name = 'transactions/transaction_report.html'
    model = Transaction
    balance = 0
    context_object_name = 'report_list'
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(
            account = self.request.user.account
        )
        
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')
        
        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
            
            queryset = queryset.filter(timestamp__date__gte = start_date, timestamp__date__lte = end_date)
            
            self.balance = queryset.filter(timestamp__date__gte = start_date, timestamp__date__lte = end_date).aggregate(Sum('amount'))['amount__sum']
        
        else:
            self.balance = self.request.user.account.balance
        return queryset.distinct()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account' : self.request.user.account
        })
        return context

class PayLoanView(LoginRequiredMixin, View):
    def get(self, request, loan_id):
        loan = get_object_or_404(Transaction, id=loan_id)
        
        if loan.loan_approve:
            user_account = loan.account
            if loan.amount < user_account.balance:
                user_account.balance -= loan.amount
                loan.balance_after_transaction = user_account.balance
                user_account.save()
                
                loan.transaction_type = LOAN_PAID
                loan.save()
                return redirect(reverse_lazy('loan_list'))
            else:
                messages.error(self.request, f"Loan amount is geater than available balance")
                return redirect(reverse_lazy('loan_list'))

class LoanListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/loan_request.html'
    context_object_name = 'loans'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Transaction.objects.filter(account=self.request.user.account, transaction_type = LOAN)
        return queryset
    
class MoneyTransferView(TransactionCreateMixin):
    template_name = 'transactions/money_transfer_form.html'
    form_class = MoneyTransferForm
    title = 'Money Transfer'
    
    def get_initial(self):
        initial = {'transaction_type' : TRANSFER}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        recipient_account = form.recipient_account
        total_bank_balance = UserBankAccount.objects.aggregate(Sum('balance'))['balance__sum'] or 0
        if total_bank_balance < amount:
            return HttpResponse("The bank is bankrupt. Money Transfer cannot be processed.")
        
        account = self.request.user.account
        account.balance -= amount
        recipient_account.balance += amount
        account.save(update_fields=['balance'])
        recipient_account.save(update_fields=['balance'])

        Transaction.objects.create(
            account = recipient_account,
            amount = amount,
            balance_after_transaction = recipient_account.balance,
            transaction_type = RECEIVE
        )
        
        messages.success(self.request, f'Successfully transferred {amount}$ to account {recipient_account}')
        
        send_transaction_email(
                user = self.request.user,
                subject = "Money Transfer",
                amount = amount,
                template = "transactions/sender_email.html",
                user2 = recipient_account
            )
        send_transaction_email(
                user = recipient_account.user,
                subject = "Money Receive",
                amount = amount,
                template = "transactions/receiver_email.html",
                user2 = self.request.user.account
            )
        
        return super().form_valid(form)