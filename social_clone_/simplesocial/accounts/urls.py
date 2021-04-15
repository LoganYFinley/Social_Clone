from django.urls import path
# as to not confuse them with our own views
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"

# 'Loginview' and 'LogoutView' are premade from 'django.contrib.auth'
# login needs a template, logout has a premade template from django
urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name = 'logout'),
    path('signup', views.Signup.as_view(), name = 'signup'),
]
