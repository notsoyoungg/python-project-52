from django.test import TestCase
from django.urls import reverse
from .models import Statuses
from task_manager.users.models import SiteUser
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# Create your tests here.


class TestStatuses(TestCase):

    fixtures = ['task.yaml', 'status.yaml', 'label.yaml', 'user.yaml']

    def setUp(self):
        self.test_status = Statuses.objects.get(pk=1)
        self.test_status2 = Statuses.objects.get(pk=2)
        self.test_user1 = SiteUser.objects.get(pk=1)

    def test_status_create_view(self):
        user = self.test_user1
        self.client.force_login(user)
        url = reverse('create_status')
        response1 = self.client.get(url)
        data = {'name': 'В работе'}
        response2 = self.client.post(url, data)
        storage = messages.get_messages(response2.wsgi_request)
        message = list(storage)[0]
        status = Statuses.objects.get(name='В работе')
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 302)
        self.assertEqual(message.message, 'Статус успешно создан')
        self.assertRedirects(response2, reverse('statuses_list'))
        self.assertTrue(status)

    def test_status_update_view(self):
        user = self.test_user1
        self.client.force_login(user)
        url = reverse('status_update', args=(1,))
        response1 = self.client.get(url)
        data = {'name': 'Исполнено'}
        response2 = self.client.post(url, data)
        storage = messages.get_messages(response2.wsgi_request)
        message = list(storage)[0]
        status = Statuses.objects.get(name='Исполнено')
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 302)
        self.assertEqual(message.message, 'Статус успешно изменён')
        self.assertRedirects(response2, reverse('statuses_list'))
        self.assertTrue(status)

    def test_status_delete_view(self):
        status_id = self.test_status2.pk
        status_name = self.test_status2.name
        user = self.test_user1
        self.client.force_login(user)
        url = reverse('status_delete', args=(status_id,))
        response1 = self.client.get(url)
        response2 = self.client.post(url)
        storage = messages.get_messages(response2.wsgi_request)
        message = list(storage)[0]
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 302)
        self.assertEqual(message.message, 'Статус успешно удалён')
        self.assertRedirects(response2, reverse('statuses_list'))
        with self.assertRaises(ObjectDoesNotExist):
            Statuses.objects.get(name=status_name)
