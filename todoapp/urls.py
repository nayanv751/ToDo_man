from django.urls import path 
from .views import *

urlpatterns = [
    path('', login_page),
    path('register_page/', register_page, name="register_page"),
    path('recovery_password_page/', recovery_password_page, name="recovery_password_page"),
    path('profile_page/', profile_page, name="profile_page"),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('sign_out/', login, name="sign_out"),
    path('profile_update/', profile_update, name="profile_update"),
]