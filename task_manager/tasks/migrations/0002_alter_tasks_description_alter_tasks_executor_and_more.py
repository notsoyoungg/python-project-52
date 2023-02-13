# Generated by Django 4.1.5 on 2023-02-03 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0001_initial'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='executor',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='statuses.statuses', verbose_name='Статус'),
        ),
    ]