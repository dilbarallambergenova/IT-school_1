from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth import logout

class SignUpView(CreateView):
    form_class=CustomUserCreationForm
    success_url=reverse_lazy('login')
    template_name='registration/signup.html'
def custom_logout(request):
    logout(request)
    return redirect("home")