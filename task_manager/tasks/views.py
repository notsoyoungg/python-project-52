from django.urls import reverse_lazy
from django.views.generic import CreateView
from task_manager.tasks.models import Tasks
from task_manager.tasks.forms import TaskForm
from django.views import generic
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic.detail import DetailView

# Create your views here.
class TaskCreationView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/login/'
    form_class = TaskForm
    template_name = 'form.html'
    success_message = 'Задача успешно создана'
    success_url = reverse_lazy('tasks_list')
    extra_context = {'header': 'Создать задачу',
                     'button': 'Создать'}

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskListView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    model = Tasks


class TaskDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = Tasks


class TaskDeleteView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    login_url = '/login/'
    model = Tasks
    success_message = 'Задача успешно удалена'
    success_url = reverse_lazy('tasks_list')
    template_name = 'confirm_delete.html'
    context_object_name = 'object'
    extra_context = {'obj_name': 'задачи'}

    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()
        if request.user != task.creator:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/login/'
    form_class = TaskForm
    template_name = 'form.html'
    extra_context = {'header': 'Изменение задачи',
                     'button': 'Изменить'}
    model = Tasks
    success_message = 'Задача успешно изменена'
    success_url = reverse_lazy('tasks_list')
    template_name = 'form.html'
    