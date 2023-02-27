from django.urls import reverse_lazy
from django.views.generic import CreateView
from task_manager.labels.models import Label
from task_manager.labels.forms import LabelForm
from django.views import generic
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from task_manager.mixins import ProtectionCheckMixin

# Create your views here.


class LabelCreationView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """User registration view."""
    login_url = '/login/'
    form_class = LabelForm
    success_message = _('Label succesfully created')
    success_url = reverse_lazy('label_list')
    template_name = 'form.html'
    extra_context = {'header': _('Create label'),
                     'button': _('Create')}


class LabelListView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    model = Label


class LabelDeleteView(LoginRequiredMixin,
                      SuccessMessageMixin,
                      ProtectionCheckMixin,
                      generic.DeleteView):
    login_url = '/login/'
    model = Label
    success_message = _('Label succesfully deleted')
    success_url = reverse_lazy('label_list')
    template_name = 'confirm_delete.html'
    context_object_name = 'object'
    extra_context = {'obj_name': _('Labels')}
    error_message = _('Cannot delete label because it is in use')


class LabelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/login/'
    form_class = LabelForm
    model = Label
    success_message = _('Label succesfully changed')
    success_url = reverse_lazy('label_list')
    template_name = 'form.html'
    extra_context = {'header': _('Label change'),
                     'button': _('Change')}
