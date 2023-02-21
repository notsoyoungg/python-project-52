from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _


# Create your models here.
class SiteUser(AbstractUser):
    """Model representing a user account."""
    # first_name = models.CharField(max_length=150, verbose_name='Имя')
    # last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    first_name = models.CharField(max_length=150, verbose_name=_('Name'))
    last_name = models.CharField(max_length=150, verbose_name=_('Surname'))

    def __str__(self):
        """Represent an instance as a string."""
        return f'{self.first_name} {self.last_name}'
