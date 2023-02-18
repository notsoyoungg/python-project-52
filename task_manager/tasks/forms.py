from django import forms
from django.forms import ModelForm
from task_manager.tasks.models import Tasks
from task_manager.users.models import SiteUser
from task_manager.labels.models import Label

class TaskForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        label='Метки'
    )
    class Meta:
        model = Tasks
        fields = ['name', 'description', 'status', 'executor', 'labels']
        # widgets = {
        #     'description': forms.Textarea(attrs={'required': False}),
        # }
