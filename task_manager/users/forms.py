from django.contrib.auth.forms import UserCreationForm
from task_manager.users.models import SiteUser


class UserCreation(UserCreationForm):
    """Site user creation form."""

    class Meta(UserCreationForm.Meta):
        model = SiteUser
        fields = ('first_name', 'last_name', 'username')
