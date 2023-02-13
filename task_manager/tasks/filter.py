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
    uncategorized = django_filters.BooleanFilter(field_name='creator', lookup_expr='istrue')


    class Meta:
        model = Tasks
        fields = ['status', 'executor', 'labels', 'creator']
        # widgets = {
        #     'labels': forms.ChoiceField(choices=Label.objects.all(), forms.Select = {'classs': 'form-control'})
        # }

    
    @property
    def qs(self):
        parent = super().qs
        creator = getattr(self.request, 'user', None)

        return parent.filter(creator=creator)
