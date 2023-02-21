from django.db import models
from task_manager.users.models import SiteUser
from task_manager.statuses.models import Statuses
from task_manager.labels.models import Label
from django.utils.translation import gettext as _

# Create your models here.


class Tasks(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Name'))
    creator = models.ForeignKey(SiteUser, on_delete=models.PROTECT)
    description = models.TextField(verbose_name=_('Description'),
                                   null=True,
                                   blank=True)
    status = models.ForeignKey(Statuses, on_delete=models.PROTECT, verbose_name=_('Status'))
    executor = models.ForeignKey(SiteUser, on_delete=models.PROTECT,
                                 verbose_name=_('Executor'),
                                 related_name='executor',
                                 null=True,
                                 blank=True)
    labels = models.ManyToManyField(Label, verbose_name=_('Labels'),
                                    through="TasksLabels",
                                    blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.name


class TasksLabels(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    labels = models.ForeignKey(Label, on_delete=models.PROTECT)
