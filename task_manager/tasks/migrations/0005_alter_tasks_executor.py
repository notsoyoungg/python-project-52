# Generated by Django 4.1.5 on 2023-02-06 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0004_tasks_labels_alter_tasks_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='executor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='executor_id', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель'),
        ),
    ]
