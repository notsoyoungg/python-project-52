# Generated by Django 4.1.5 on 2023-02-17 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0002_statuses_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statuses',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
    ]
