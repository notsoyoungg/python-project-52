import django_filters
from .models import Tasks
from task_manager.labels.models import Label
from task_manager.statuses.models import Statuses
from task_manager.users.models import SiteUser
from django import forms


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(queryset=Statuses.objects.all(),
        label='Статус',
        widget=forms.Select(attrs={'class': 'form-control'}))
    executor = django_filters.ModelChoiceFilter(queryset=SiteUser.objects.all(),
        label='Исполнитель',
        widget=forms.Select(attrs={'class': 'form-control'}))
    labels = django_filters.ModelChoiceFilter(queryset=Label.objects.all(),
        label='Метка',
        widget=forms.Select(attrs={'class': 'form-control'}))
    self_tasks = django_filters.BooleanFilter(field_name='creator', method='filter_only_current_user',
        label='Только свои задачи',
        widget=forms.CheckboxInput(attrs={'class': "form-check", 'name': 'jopa'}))
    class Meta:
        model = Tasks
        fields = ['status', 'executor', 'labels']
        

    def filter_only_current_user(self, queryset, name, value):
        if value:
            return queryset.filter(creator=self.request.user)
        return queryset
