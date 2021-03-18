# Generated by Django 3.1.7 on 2021-03-18 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20210318_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskpriority',
            name='typedescription',
        ),
        migrations.AlterField(
            model_name='taskpriority',
            name='taskpriority',
            field=models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='LOW', max_length=6),
        ),
    ]
