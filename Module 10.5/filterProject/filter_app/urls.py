
from django.urls import path
from . import views

urlpatterns = [
    path('geeksforgeeks/', views.geeksforgeeks),
    path('earthly/', views.earthly),
]
