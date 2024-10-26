from django.shortcuts import render
from .models import Participant
from .forms import ParticipantForm
from django.views.generic import CreateView
from django.urls import reverse_lazy ,reverse
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.

class UserCreateView(CreateView):
    model=Participant
    form_class =ParticipantForm
    template_name ="users/register.html"
    success_url = reverse_lazy('login')


class LoginCustomView(LoginView):
    template_name='users/login.html'
    #def get_success_url(self):
    #    return reverse('listeViewconf')

class LogoutCustomView(LogoutView):
    next_page= reverse_lazy('login')