# Generated by Django 4.1.5 on 2023-02-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0003_alter_label_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]