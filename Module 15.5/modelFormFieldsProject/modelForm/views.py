from django.shortcuts import render
from .forms import MediumForm, MediumForm2

def home(request):
    return render(request, 'index.html')

def medium_form(request):
    form1 = MediumForm()
    form2 = MediumForm2()

    if request.method == 'POST':
        if 'submit_form1' in request.POST:
            form1 = MediumForm(request.POST)
            if form1.is_valid():
                form1.save()
        elif 'submit_form2' in request.POST:
            form2 = MediumForm2(request.POST, request.FILES)
            if form2.is_valid():
                form2.save()

    return render(request, 'medium.html', {'form1': form1, 'form2': form2})
