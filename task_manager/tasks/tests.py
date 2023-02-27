from django.test import TestCase
from django.urls import reverse
from .models import Tasks, Label, Statuses
from task_manager.users.models import SiteUser
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# Create your tests here.


class TestTask(TestCase):

    fixtures = ['task.yaml', 'status.yaml', 'label.yaml', 'user.yaml']

    def setUp(self):
        self.label = Label.objects.get(pk=1)
        self.status = Statuses.objects.get(pk=1)
        self.test_user1 = SiteUser.objects.get(pk=1)
        self.task = Tasks.objects.get(pk=1)

    def test_task_create_view(self):
        user = self.test_user1
        self.client.force_login(user)
        url = reverse('create_task')
        response1 = self.client.get(url)
        data = {'name': 'Таска',
                'description': 'описание задачи',
                'status': 1,
                'executor': 1,
                'labels': 1
                }
        response2 = self.client.post(url, data)
        storage = messages.get_messages(response2.wsgi_request)
        message = list(storage)[0]
        task = Tasks.objects.get(name='Таска')
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 302)
        self.assertEqual(message.message, 'Задача успешно создана')
        self.assertRedirects(response2, reverse('tasks_list'))
        self.assertTrue(task)

    def test_task_update_view(self):
        user = self.test_user1
        self.client.force_login(user)
        url = reverse('task_update', args=(1,))
        response1 = self.client.get(url)
        data = {'name': 'Обновленная таска',
                'description': 'описание задачи',
                'status': 1,
                'executor': 1,
                'labels': 1
                }
        response2 = self.client.post(url, data)
        storage = messages.get_messages(response2.wsgi_request)
        message = list(storage)[0]
        task = Tasks.objects.get(name='Обновленная таска')
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 302)
        self.assertEqual(message.message, 'Задача успешно изменена')
        self.assertRedirects(response2, reverse('tasks_list'))
        self.assertTrue(task)

    def test_task_delete_view(self):
        task_id = self.task.pk
        user = self.test_user1
        self.client.force_login(user)
        url = reverse('task_delete', args=(task_id,))
        response1 = self.client.get(url)
        response2 = self.client.post(url)
        storage = messages.get_messages(response2.wsgi_request)
        message = list(storage)[0]
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 302)
        self.assertEqual(message.message, 'Задача успешно удалена')
        self.assertRedirects(response2, reverse('tasks_list'))
        with self.assertRaises(ObjectDoesNotExist):
            Tasks.objects.get(name='Task')
