from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class SiteUser(AbstractUser):
    """Model representing a user account."""
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    def __str__(self):
        """Represent an instance as a string."""
        return f'{self.first_name} {self.last_name}'
