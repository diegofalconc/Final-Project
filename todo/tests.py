from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task
import datetime
from django.urls import reverse
# Create your tests here.
class TaskTest(TestCase):
    def setUp(self):
        self.task=Task(taskname='Homework')

    def test_string(self):
        self.assertEqual(str(self.task), 'Homework')

    def test_tablename(self):
        self.assertEqual(str(Task._meta.db_table), 'task')

class New_Task_Authentication_Test(TestCase):
    def setUp(self):
         self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
         self.type=Task.objects.create(taskname='homework', taskpriority='Low', user=self.test_user, taskentrydate=datetime.date(2021,3,20), taskdescription="bam")

    def test_redirect_if_not_logged_in(self):
         response = self.client.get(reverse('newtask'))
         self.assertRedirects(response, '/accounts/login/?next=/todo/newTask/')

