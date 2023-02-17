from django.urls import reverse_lazy
from django.views.generic import CreateView
from task_manager.labels.models import Label
from task_manager.labels.forms import LabelForm
from django.views import generic
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class LabelCreationView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """User registration view."""
    login_url = '/login/'
    form_class = LabelForm
    success_message = 'Метка добавлена'
    success_url = reverse_lazy('label_list')
    template_name = 'form.html'
    extra_context = {'header': 'Создать метку',
                     'button': 'Создать'}



class LabelListView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    model = Label


class LabelDeleteView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Label
    success_message = 'Метка удалена'
    success_url = reverse_lazy('label_list')
    template_name = 'confirm_delete.html'
    context_object_name = 'object'
    extra_context = {'obj_name': 'метки'}


class LabelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = LabelForm
    model = Label
    success_message = 'Метка обновлена'
    success_url = reverse_lazy('label_list')
    template_name = 'form.html'
    extra_context = {'header': 'Изменение метки',
                     'button': 'Изменить'}
