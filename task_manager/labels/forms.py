from django.forms import ModelForm
from task_manager.labels.models import Label

class LabelForm(ModelForm):
    class Meta:
        model = Label
        fields = ['name']
