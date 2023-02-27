from django.test import TestCase
from django.urls import reverse
from .models import SiteUser
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# Create your tests here.


class TestUsers(TestCase):

    fixtures = ['task.yaml', 'status.yaml', 'label.yaml', 'user.yaml']

    def setUp(self):
        self.test_user1 = SiteUser.objects.get(pk=1)
        self.test_user2 = SiteUser.objects.get(pk=2)

    def test_user_create_view(self):
        url = reverse('register')
        response1 = self.client.get(url)
        data = {'first_name': 'Perrito',
                'last_name': 'jobs',
                'username': 'testuser',
                'password1': '1234',
                'password2': '1234'}
        response2 = self.client.post(url, data)
        storage = messages.get_messages(response2.wsgi_request)
        message = list(storage)[0]
        user = SiteUser.objects.get(username='testuser')
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 302)
        self.assertEqual(message.message, 'Пользователь успешно зарегистрирован')
        self.assertRedirects(response2, '/login/')
        self.assertTrue(user)

    def test_user_update_view(self):
        user = self.test_user1
        self.client.force_login(user)
        url = reverse('user_update', args=(1,))
        response1 = self.client.get(url)
        data = {'first_name': 'Perrito',
                'last_name': 'jobs',
                'username': 'second_testuser',
                'password1': '1234',
                'password2': '1234'}
        response2 = self.client.post(url, data)
        storage = messages.get_messages(response2.wsgi_request)
        message = list(storage)[0]
        user = SiteUser.objects.get(username='testuser2')
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 302)
        self.assertEqual(message.message, 'Пользователь успешно изменён')
        self.assertRedirects(response2, '/users/')
        self.assertTrue(user)

    def test_user_delete_view(self):
        user = self.test_user2
        self.client.force_login(user)
        url = reverse('user_delete', args=(user.pk,))
        response1 = self.client.get(url)
        response2 = self.client.post(url)
        storage = messages.get_messages(response2.wsgi_request)
        message = list(storage)[0]
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 302)
        self.assertEqual(message.message, 'Пользователь успешно удалён')
        self.assertRedirects(response2, '/users/')
        with self.assertRaises(ObjectDoesNotExist):
            SiteUser.objects.get(username=user.username)
