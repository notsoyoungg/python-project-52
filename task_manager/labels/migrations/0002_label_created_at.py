# Generated by Django 4.1.5 on 2023-02-11 12:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]