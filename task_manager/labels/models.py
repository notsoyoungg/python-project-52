from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class Label(models.Model):
    # name = models.CharField(max_length=100, verbose_name='Имя')
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.name
