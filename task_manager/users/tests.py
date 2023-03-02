from django.test import TestCase
from django.urls import reverse
from .models import SiteUser
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext as _
import json

# Create your tests here.


class TestUsers(TestCase):

    fixtures = ['task.yaml', 'status.yaml', 'label.yaml', 'user.yaml']

    def setUp(self):
        self.test_user1 = SiteUser.objects.get(pk=1)
        self.test_user2 = SiteUser.objects.get(pk=2)

    def test_user_create_view(self):
        with open(('task_manager/fixtures/user_test_data.json')) as content:
            dump_data = json.load(content)
            url = reverse('register')
            response1 = self.client.get(url)
            response2 = self.client.post(url, dump_data['user'])
            user = SiteUser.objects.get(username='testuser')
            messsages = map(lambda item: item.message,
                            messages.get_messages(response2.wsgi_request))
            self.assertIn(_('User succesfully registered'), messsages)
            self.assertEqual(response1.status_code, 200)
            self.assertEqual(response2.status_code, 302)
            self.assertRedirects(response2, '/login/')
            self.assertTrue(user)

    def test_user_update_view(self):
        with open(('task_manager/fixtures/user_test_data.json')) as content:
            dump_data = json.load(content)
            user = self.test_user1
            self.client.force_login(user)
            url = reverse('user_update', args=(1,))
            response1 = self.client.get(url)
            response2 = self.client.post(url, dump_data['updated_user'])
            user = SiteUser.objects.get(username='testuser2')
            messsages = map(lambda item: item.message,
                            messages.get_messages(response2.wsgi_request))
            self.assertIn(_('User succesfully changed'), messsages)
            self.assertEqual(response1.status_code, 200)
            self.assertEqual(response2.status_code, 302)
            self.assertRedirects(response2, '/users/')
            self.assertTrue(user)

    def test_user_delete_view(self):
        user = self.test_user2
        self.client.force_login(user)
        url = reverse('user_delete', args=(user.pk,))
        response1 = self.client.get(url)
        response2 = self.client.post(url)
        messsages = map(lambda item: item.message, messages.get_messages(response2.wsgi_request))
        self.assertIn(_('User succesfully deleted'), messsages)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 302)
        self.assertRedirects(response2, '/users/')
        with self.assertRaises(ObjectDoesNotExist):
            SiteUser.objects.get(username=user.username)
