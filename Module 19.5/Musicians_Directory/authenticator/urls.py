from django.urls import path
from authenticator.views import *

urlpatterns = [
    path('signup/', SignupFormView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/update/', EditProfileView.as_view(), name='edit_profile'),
    path('profile/update/change_password/', UserPassChangeView.as_view(), name='passchange'),
]
