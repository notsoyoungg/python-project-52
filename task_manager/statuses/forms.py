from django.forms import ModelForm
from task_manager.statuses.models import Statuses


class StatuseForm(ModelForm):
    class Meta:
        model = Statuses
        fields = ['name']
