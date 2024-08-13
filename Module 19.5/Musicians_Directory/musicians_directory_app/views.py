from django.shortcuts import render
from musicians_directory_app.models import *
from musicians_directory_app.forms import *
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

class HomeView(ListView):
    model = AlbumModel
    template_name = 'home.html'
    context_object_name = 'data'

class MusicianView(LoginRequiredMixin, CreateView):
    model = MusicianModel
    form_class = MusicianForm
    template_name = 'common_form.html'
    success_url = reverse_lazy('add_musician')
    
    def form_valid(self, form):
        messages.success(self.request, 'Add Musician Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Enter Valid Musician Information')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["type"] = 'Add Musician'
        context["bg"] = 'success'
        return context
    
class EditMusicianView(LoginRequiredMixin, UpdateView):
    model = MusicianModel
    form_class = MusicianForm
    template_name = 'common_form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Update Musician Data Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Enter Valid Musician Information')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["type"] = 'Update Musician'
        context["bg"] = 'warning'
        return context
    
class AlbumView(LoginRequiredMixin, CreateView):
    model = AlbumModel
    form_class = AlbumForm
    template_name = 'common_form.html'
    success_url = reverse_lazy('add_album')
    
    def form_valid(self, form):
        messages.success(self.request, 'Add Album Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Enter Valid Album Information')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["type"] = 'Add Album'
        context["bg"] = 'success'
        return context
    
class EditAlbumView(LoginRequiredMixin, UpdateView):
    model = AlbumModel
    form_class = AlbumForm
    template_name = 'common_form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Update Album Data Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Enter Valid Album Information')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["type"] = 'Update Album'
        context["bg"] = 'warning'
        return context
    
class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = AlbumModel
    template_name = 'common_form.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        messages.success(self.request, 'Album deleted successfully')
        return reverse_lazy('profile')
    
    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["type"] = 'Delete Album'
        context["bg"] = 'danger'
        context["delete"] = 'Are you delate this Album?'
        return context
    