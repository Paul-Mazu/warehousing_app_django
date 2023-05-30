from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("account:login")
    template_name = "registration/signup.html"


class CustomLogin(SuccessMessageMixin, LoginView):
    # template_name = 'users/login.html'
    success_url = "stock:index"
    success_message = "Welcome to your profile"
    


class CustomLogout(SuccessMessageMixin, LogoutView):
    # template_name = 'users/login.html'
    success_url = "stock:index"
    success_message = "Logged out successfully!"
