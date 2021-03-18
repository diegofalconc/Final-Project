from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    HIGH = 'High'
    MEDIUM = 'Medium'
    LOW = 'Low'

    Priority = (
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    )
    taskname=models.CharField(max_length=255)
    taskpriority=models.CharField(max_length=6, choices=Priority, default="LOW")
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    taskentrydate=models.DateField()
    taskdescription=models.TextField()

    def __str__(self):
        return self.taskname
    
    class Meta:
        db_table='task'
