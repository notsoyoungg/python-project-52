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
from django.utils.translation import gettext as _

# Create your views here.


class RegistrationView(SuccessMessageMixin, CreateView):
    """User registration view."""
    form_class = UserCreation
    text1 = _('User succesfully registered')
    text2 = _('Registration')
    text3 = _('Register')
    # success_message = 'Пользователь успешно зарегистрирован'
    success_message = text1
    success_url = reverse_lazy('login')
    template_name = 'form.html'
    # extra_context = {'header': 'Регистрация',
    #                  'button': 'Зарегистрировать'}
    extra_context = {'header': text2,
                     'button': text3}


class UserListView(generic.ListView):
    model = SiteUser


class UserDeleteView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    login_url = '/login/'
    model = SiteUser
    text1 = _('User succesfully deleted')
    text2 = _('user')
    # success_message = 'Пользователь успешно удалён'
    success_message = text1
    success_url = reverse_lazy('user_list')
    template_name = 'confirm_delete.html'
    context_object_name = 'object'
    # extra_context = {'obj_name': 'пользователя'}
    extra_context = {'obj_name': text2}

    def dispatch(self, request, *args, **kwargs):
        site_user = self.get_object()
        if request.user != site_user:
            text3 = _('no rights to change')
            # messages.error(request, 'нет прав на изменение')
            messages.error(request, text3)
            return HttpResponseRedirect(reverse_lazy('user_list'))

        return super().dispatch(request, *args, **kwargs)


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/login/'
    form_class = UserCreation
    model = SiteUser
    text1 = _('User succesfully changed')
    text2 = _('User change')
    text3 = _('Change')
    # success_message = 'Пользователь успешно изменён'
    success_message = text1
    success_url = reverse_lazy('user_list')
    template_name = 'form.html'
    # extra_context = {'header': 'Изменение пользователя',
    #                  'button': 'Изменить'}
    extra_context = {'header': text2,
                     'button': text3}

    def dispatch(self, request, *args, **kwargs):
        site_user = self.get_object()
        if request.user != site_user:
            text4 = _('no rights to change')
            # messages.error(request, 'нет прав на изменение')
            messages.error(request, text4)
            return HttpResponseRedirect(reverse_lazy('user_list'))

        return super().dispatch(request, *args, **kwargs)
