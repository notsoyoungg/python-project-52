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
from django.utils.translation import gettext as _

# Create your views here.


class LabelCreationView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """User registration view."""
    login_url = '/login/'
    form_class = LabelForm
    text1 = _('Label succesfully created')
    # success_message = 'Метка успешно создана'
    success_message = text1
    success_url = reverse_lazy('label_list')
    template_name = 'form.html'
    text2 = _('Create label')
    text3 = _('Create')
    # extra_context = {'header': 'Создать метку',
    #                  'button': 'Создать'}
    extra_context = {'header': text2,
                     'button': text3}


class LabelListView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    model = Label


class LabelDeleteView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    login_url = '/login/'
    model = Label
    text1 = _('Label succesfully deleted')
    text2 = _('Labels')
    # success_message = 'Метка успешно удалена'
    success_message = text1
    success_url = reverse_lazy('label_list')
    template_name = 'confirm_delete.html'
    context_object_name = 'object'
    # extra_context = {'obj_name': 'метки'}
    extra_context = {'obj_name': text2}

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except ProtectedError:
            text3 = _('Cannot delete label because it is in use')
            # messages.error(request, 'Невозможно удалить метку, потому что она используется')
            messages.error(request, text3)
            return redirect('statuses_list')


class LabelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/login/'
    form_class = LabelForm
    model = Label
    text1 = _('Label succesfully changed')
    text2 = _('Label change')
    text3 = _('Change')
    # success_message = 'Метка успешно изменена'
    success_message = text1
    success_url = reverse_lazy('label_list')
    template_name = 'form.html'
    # extra_context = {'header': 'Изменение метки',
    #                  'button': 'Изменить'}
    extra_context = {'header': text2,
                     'button': text3}
