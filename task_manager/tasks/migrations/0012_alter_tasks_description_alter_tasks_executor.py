# Generated by Django 4.1.5 on 2023-02-21 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0011_alter_tasks_description_alter_tasks_executor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='executor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='executor', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель'),
        ),
    ]
