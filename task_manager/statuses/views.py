from django.urls import reverse_lazy
from django.views.generic import CreateView
from task_manager.statuses.models import Statuses
from task_manager.statuses.forms import StatuseForm
from django.views import generic
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from task_manager.mixins import ProtectionCheckMixin

# Create your views here.


class StatuseCreationView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """User registration view."""
    login_url = '/login/'
    form_class = StatuseForm
    template_name = 'form.html'
    extra_context = {'header': _('Create status'),
                     'button': _('Create')}
    success_message = _('Status succesfully created')
    success_url = reverse_lazy('statuses_list')


class StatusesListView(LoginRequiredMixin, SuccessMessageMixin, generic.ListView):
    login_url = '/login/'
    model = Statuses


class StatusDeleteView(LoginRequiredMixin,
                       SuccessMessageMixin,
                       ProtectionCheckMixin,
                       generic.DeleteView):
    login_url = '/login/'
    model = Statuses
    template_name = 'confirm_delete.html'
    context_object_name = 'object'
    extra_context = {'obj_name': _('status')}
    success_message = _('Status succesfully deleted')
    success_url = reverse_lazy('statuses_list')
    error_message = _('Cannot delete status because it is in use')


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/login/'
    form_class = StatuseForm
    model = Statuses
    success_message = _('Status succesfully changed')
    success_url = reverse_lazy('statuses_list')
    template_name = 'form.html'
    extra_context = {'header': _('Status change'),
                     'button': _('Change')}
