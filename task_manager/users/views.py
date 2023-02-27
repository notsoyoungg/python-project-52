from django.urls import reverse_lazy
from django.views.generic import CreateView
from task_manager.users.forms import UserCreation
from django.views import generic
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from task_manager.mixins import PermRequiredMixin
from django.contrib.auth import get_user_model

# Create your views here.


class RegistrationView(SuccessMessageMixin, CreateView):
    """User registration view."""
    form_class = UserCreation
    success_message = _('User succesfully registered')
    success_url = reverse_lazy('login')
    template_name = 'form.html'
    extra_context = {'header': _('Registration'),
                     'button': _('Register')}


class UserListView(generic.ListView):
    model = get_user_model()


class UserDeleteView(LoginRequiredMixin,
                     SuccessMessageMixin,
                     PermRequiredMixin,
                     generic.DeleteView):
    login_url = '/login/'
    model = get_user_model()
    success_message = _('User succesfully deleted')
    success_url = reverse_lazy('user_list')
    template_name = 'confirm_delete.html'
    context_object_name = 'object'
    extra_context = {'obj_name': _('user')}


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, PermRequiredMixin, UpdateView):
    login_url = '/login/'
    form_class = UserCreation
    model = get_user_model()
    success_message = _('User succesfully changed')
    success_url = reverse_lazy('user_list')
    template_name = 'form.html'
    extra_context = {'header': _('User change'),
                     'button': _('Change')}
