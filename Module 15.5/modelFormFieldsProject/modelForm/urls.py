from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('medium/', views.medium_form, name='medium'),
]
