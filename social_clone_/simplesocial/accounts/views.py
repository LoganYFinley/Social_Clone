from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms

# Create your views here.
class Signup(CreateView):
    form_class = forms.UserCreateForm
    # return user to login page after successful sign-up once they hit submit
    success_url = reverse_lazy('login') 
    template_name = 'accounts/signup.html'

