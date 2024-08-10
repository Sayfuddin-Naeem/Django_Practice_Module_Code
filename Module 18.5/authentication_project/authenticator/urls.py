from django.urls import path
from authenticator.views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup/', sign_up, name='sign_up'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('pass_change/', pass_change, name='passchange'),
    path('pass_change2/', pass_change2, name='passchange2'),
]
