from django.contrib.auth.views import LoginView as LoginViewBase,\
    LogoutView as LogoutViewBase
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(LoginViewBase):
    template_name = 'core/login.html'


class LogoutView(LoginRequiredMixin, LogoutViewBase):
    next_page = 'core:login'
