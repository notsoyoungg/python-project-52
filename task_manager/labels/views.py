from django.urls import reverse_lazy
from django.views.generic import CreateView
from task_manager.labels.models import Label
from task_manager.labels.forms import LabelForm
from django.views import generic
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.deletion import ProtectedError
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.


class LabelCreationView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """User registration view."""
    login_url = '/login/'
    form_class = LabelForm
    success_message = 'Метка успешно создана'
    success_url = reverse_lazy('label_list')
    template_name = 'form.html'
    extra_context = {'header': 'Создать метку',
                     'button': 'Создать'}


class LabelListView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    model = Label


class LabelDeleteView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    login_url = '/login/'
    model = Label
    success_message = 'Метка успешно удалена'
    success_url = reverse_lazy('label_list')
    template_name = 'confirm_delete.html'
    context_object_name = 'object'
    extra_context = {'obj_name': 'метки'}

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, 'Невозможно удалить метку, потому что она используется')
            return redirect('statuses_list')


class LabelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/login/'
    form_class = LabelForm
    model = Label
    success_message = 'Метка успешно изменена'
    success_url = reverse_lazy('label_list')
    template_name = 'form.html'
    extra_context = {'header': 'Изменение метки',
                     'button': 'Изменить'}
