from django.urls import reverse_lazy
from django.views.generic import CreateView
from task_manager.statuses.models import Statuses
from task_manager.statuses.forms import StatuseForm
from django.views import generic
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models.deletion import ProtectedError
from django.utils.translation import gettext as _

# Create your views here.


class StatuseCreationView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """User registration view."""
    login_url = '/login/'
    form_class = StatuseForm
    template_name = 'form.html'
    text1 = _('Status succesfully created')
    text2 = _('Create status')
    text3 = _('Create')
    # extra_context = {'header': 'Создать статус',
    #                  'button': 'Создать'}
    extra_context = {'header': text2,
                     'button': text3}
    # success_message = 'Статус успешно создан'
    success_message = text1
    success_url = reverse_lazy('statuses_list')


class StatusesListView(LoginRequiredMixin, SuccessMessageMixin, generic.ListView):
    login_url = '/login/'
    model = Statuses


class StatusDeleteView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    login_url = '/login/'
    model = Statuses
    template_name = 'confirm_delete.html'
    context_object_name = 'object'
    text1 = _('Status succesfully deleted')
    text2 = _('status')
    # extra_context = {'obj_name': 'статуса'}
    extra_context = {'obj_name': text2}
    # success_message = 'Статус успешно удалён'
    success_message = text1
    success_url = reverse_lazy('statuses_list')

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except ProtectedError:
            text3 = _('Cannot delete status because it is in use')
            # messages.error(request, 'Невозможно удалить статус, потому что он используется')
            messages.error(request, text3)
            return redirect('statuses_list')


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/login/'
    form_class = StatuseForm
    model = Statuses
    text1 = _('Status succesfully changed')
    text2 = _('Status change')
    text3 = _('Change')
    # success_message = 'Статус успешно изменён'
    success_message = text1
    success_url = reverse_lazy('statuses_list')
    template_name = 'form.html'
    # extra_context = {'header': 'Изменение статуса',
    #                  'button': 'Изменить'}
    extra_context = {'header': text2,
                     'button': text3}
