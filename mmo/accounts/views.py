from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import CustomSignupForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
class SignUp(CreateView):
    model = User
    form_class = CustomSignupForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'

