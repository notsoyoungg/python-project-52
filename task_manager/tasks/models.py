from django.db import models
from task_manager.users.models import SiteUser
from task_manager.statuses.models import Statuses
from task_manager.labels.models import Label

# Create your models here.
class Tasks(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    creator = models.ForeignKey(SiteUser, on_delete=models.PROTECT)
    description = models.TextField(verbose_name='Описание')
    status = models.ForeignKey(Statuses, on_delete=models.PROTECT, verbose_name='Статус')
    executor = models.ForeignKey(SiteUser, on_delete=models.PROTECT, verbose_name='Исполнитель', related_name='executor_id')
    labels = models.ManyToManyField(Label, verbose_name='Метки')
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.name
