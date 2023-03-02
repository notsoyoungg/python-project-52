from django.urls import reverse_lazy
from django.views.generic import CreateView
from task_manager.users.forms import UserCreation
from django.views import generic
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from task_manager.mixins import ProtectionCheckMixin, ModifiedUserPassesTestMixin
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
                     ModifiedUserPassesTestMixin,
                     ProtectionCheckMixin,
                     generic.DeleteView):
    login_url = '/login/'
    error_url = 'user_list'
    model = get_user_model()
    success_message = _('User succesfully deleted')
    error_message = _('Cannot delete user because it is in use')
    success_url = reverse_lazy('user_list')
    template_name = 'confirm_delete.html'
    context_object_name = 'object'
    extra_context = {'obj_name': _('user')}


class UserUpdateView(LoginRequiredMixin,
                     SuccessMessageMixin,
                     ModifiedUserPassesTestMixin,
                     ProtectionCheckMixin,
                     UpdateView):
    login_url = '/login/'
    error_url = 'user_list'
    form_class = UserCreation
    model = get_user_model()
    success_message = _('User succesfully changed')
    error_message = _('No rights to change another user')
    success_url = reverse_lazy('user_list')
    template_name = 'form.html'
    extra_context = {'header': _('User change'),
                     'button': _('Change')}
