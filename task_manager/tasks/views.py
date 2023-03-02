from django.urls import reverse_lazy
from django.views.generic import CreateView
from task_manager.tasks.models import Tasks
from task_manager.tasks.forms import TaskForm
from django.views import generic
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import DetailView
from django.utils.translation import gettext as _
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.


class TaskCreationView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/login/'
    form_class = TaskForm
    template_name = 'form.html'
    success_message = _('Task succesfully created')
    success_url = reverse_lazy('tasks_list')
    extra_context = {'header': _('Create task'),
                     'button': _('Create')}

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskListView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    model = Tasks


class TaskDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = Tasks


class TaskDeleteView(LoginRequiredMixin,
                     SuccessMessageMixin,
                     UserPassesTestMixin,
                     generic.DeleteView):
    login_url = '/login/'
    model = Tasks
    success_message = _('Task succesfully deleted')
    success_url = reverse_lazy('tasks_list')
    template_name = 'confirm_delete.html'
    context_object_name = 'object'
    extra_context = {'obj_name': _('task')}

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.creator

    def handle_no_permission(self):
        if self.raise_exception or self.request.user.is_authenticated:
            messages.error(self.request, _('Only the author can delete a task'))
            return redirect('tasks_list')


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/login/'
    form_class = TaskForm
    template_name = 'form.html'
    extra_context = {'header': _('Tasks change'),
                     'button': _('Change')}
    model = Tasks
    success_message = _('Task succesfully changed')
    success_url = reverse_lazy('tasks_list')
    template_name = 'form.html'
