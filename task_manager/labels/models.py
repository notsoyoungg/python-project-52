from django.db import models
from django.core.exceptions import PermissionDenied

# Create your models here.
class Label(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.name
    
    def delete(self, *args, **kwargs):
        if self.tasks_set.exists():
            raise PermissionDenied("Can't delete label because it's associated with tasks")
        super().delete(*args, **kwargs)
