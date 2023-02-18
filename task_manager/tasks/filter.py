import django_filters
from .models import Tasks
from task_manager.labels.models import Label
from django import forms


class TaskFilter(django_filters.FilterSet):
    labels = django_filters.ModelChoiceFilter(queryset=Label.objects.all(),
                                              label='Метка',
                                              widget=forms.Select(attrs={'class': 'form-control'}))
    tasks = django_filters.BooleanFilter(field_name='creator',
                                         method='filter_only_current_user',
                                         label='Только свои задачи',
                                         widget=forms.CheckboxInput(attrs={'class': "form-check"}))

    class Meta:
        model = Tasks
        fields = ['status', 'executor', 'labels']

    def filter_only_current_user(self, queryset, name, value):
        if value:
            return queryset.filter(creator=self.request.user)
        return queryset
