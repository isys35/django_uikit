from django.contrib.auth.views import LoginView as LoginViewBase, \
    LogoutView as LogoutViewBase
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class LoginView(LoginViewBase):
    template_name = 'core/login.html'
    next_page = 'core:main'


class LogoutView(LoginRequiredMixin, LogoutViewBase):
    next_page = 'core:login'


class BaseView(LoginRequiredMixin, TemplateView):
    template_name = 'layout/basic.html'
