from django.urls import reverse_lazy
from django.views.generic import CreateView
from task_manager.users.models import SiteUser
from task_manager.users.forms import UserCreation
from django.views import generic
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.


class RegistrationView(SuccessMessageMixin, CreateView):
    """User registration view."""
    form_class = UserCreation
    success_message = 'Пользователь успешно зарегистрирован'
    success_url = reverse_lazy('login')
    template_name = 'form.html'
    extra_context = {'header': 'Регистрация',
                     'button': 'Зарегистрировать'}


class UserListView(generic.ListView):
    model = SiteUser


class UserDeleteView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    login_url = '/login/'
    model = SiteUser
    success_message = 'Пользователь успешно удалён'
    success_url = reverse_lazy('user_list')
    template_name = 'confirm_delete.html'
    context_object_name = 'object'
    extra_context = {'obj_name': 'пользователя'}

    def dispatch(self, request, *args, **kwargs):
        site_user = self.get_object()
        if request.user != site_user:
            messages.error(request, 'нет прав на изменение')
            return HttpResponseRedirect(reverse_lazy('user_list'))

        return super().dispatch(request, *args, **kwargs)


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/login/'
    form_class = UserCreation
    model = SiteUser
    success_message = 'Пользователь успешно изменён'
    success_url = reverse_lazy('user_list')
    template_name = 'form.html'
    extra_context = {'header': 'Изменение пользователя',
                     'button': 'Изменить'}

    def dispatch(self, request, *args, **kwargs):
        site_user = self.get_object()
        if request.user != site_user:
            messages.error(request, 'нет прав на изменение')
            return HttpResponseRedirect(reverse_lazy('user_list'))

        return super().dispatch(request, *args, **kwargs)
