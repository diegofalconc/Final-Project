# Generated by Django 3.1.7 on 2021-03-18 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20210318_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='taskpriority',
            field=models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='LOW', max_length=6),
        ),
        migrations.DeleteModel(
            name='TaskPriority',
        ),
    ]
