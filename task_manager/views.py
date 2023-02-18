from django.shortcuts import render
from django.contrib.auth import views
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


def index(request):
    return render(request, 'index.html')


class UserLoginView(SuccessMessageMixin, views.LoginView):
    next_page = reverse_lazy('index')
    success_message = 'Вы залогинены'


class UserLogoutView(SuccessMessageMixin, views.LogoutView):
    next_page = reverse_lazy('index')
    success_message = 'Вы разлогинены'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "Вы разлогинены")
        return super().dispatch(request, *args, **kwargs)
