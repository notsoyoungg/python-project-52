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

# Create your views here.
class StatuseCreationView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """User registration view."""
    login_url = '/login/'
    form_class = StatuseForm
    template_name = 'form.html'
    extra_context = {'header': 'Создать статус',
                     'button': 'Создать'}
    success_message = 'Статус успешно добавлен'
    success_url = reverse_lazy('statuses_list')


class StatusesListView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    model = Statuses


class StatusDeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = '/login/'
    model = Statuses
    template_name = 'confirm_delete.html'
    context_object_name = 'object'
    extra_context = {'obj_name': 'статуса'}
    success_message = 'Статус удален'
    success_url = reverse_lazy('statuses_list')

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, 'Статус не может быть удален')
            return redirect('statuses_list')


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    form_class = StatuseForm
    model = Statuses
    success_message = 'Статус обновлен'
    success_url = reverse_lazy('statuses_list')
    template_name = 'form.html'
    extra_context = {'header': 'Изменение статуса',
                     'button': 'Изменить'}
