from django.shortcuts import render
from django.contrib.auth import views
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _


def index(request):
    return render(request, 'index.html')


class UserLoginView(SuccessMessageMixin, views.LoginView):
    next_page = reverse_lazy('index')
    text = _('You are logged in')
    success_message = text
    # success_message = 'Вы залогинены'


class UserLogoutView(SuccessMessageMixin, views.LogoutView):
    text = _('You are logged out')
    success_message = text
    next_page = reverse_lazy('index')
    # success_message = 'Вы разлогинены'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            text = _('You are logged out')
            messages.info(request, text)
        return super().dispatch(request, *args, **kwargs)
