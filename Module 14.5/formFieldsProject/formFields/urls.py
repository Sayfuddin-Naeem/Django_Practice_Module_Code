from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('geeksforgeeks/', views.geeksforgeeks_form, name='geeksforgeeks'),
    path('ordinarycoders/', views.ordinaryCoders_form, name='ordinarycoders'),
]
