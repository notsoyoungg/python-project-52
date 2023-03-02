from django.test import TestCase
from django.urls import reverse
from .models import Label
from task_manager.users.models import SiteUser
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext as _

# Create your tests here.


class TestLabels(TestCase):

    fixtures = ['task.yaml', 'status.yaml', 'label.yaml', 'user.yaml']

    def setUp(self):
        self.test_label = Label.objects.get(pk=1)
        self.test_user1 = SiteUser.objects.get(pk=1)

    def test_label_create_view(self):
        user = self.test_user1
        self.client.force_login(user)
        url = reverse('create_label')
        response1 = self.client.get(url)
        data = {'name': 'Приоритет №1'}
        response2 = self.client.post(url, data)
        label = Label.objects.get(name='Приоритет №1')
        messsages = map(lambda item: item.message, messages.get_messages(response2.wsgi_request))
        self.assertIn(_('Label succesfully created'), messsages)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 302)
        self.assertRedirects(response2, reverse('label_list'))
        self.assertTrue(label)

    def test_label_update_view(self):
        user = self.test_user1
        self.client.force_login(user)
        url = reverse('label_update', args=(1,))
        response1 = self.client.get(url)
        data = {'name': 'Можно не делать'}
        response2 = self.client.post(url, data)
        label = Label.objects.get(name='Можно не делать')
        messsages = map(lambda item: item.message, messages.get_messages(response2.wsgi_request))
        self.assertIn(_('Label succesfully changed'), messsages)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 302)
        self.assertRedirects(response2, reverse('label_list'))
        self.assertTrue(label)

    def test_label_delete_view(self):
        label_id = self.test_label.pk
        user = self.test_user1
        self.client.force_login(user)
        url = reverse('label_delete', args=(label_id,))
        response1 = self.client.get(url)
        response2 = self.client.post(url)
        messsages = map(lambda item: item.message, messages.get_messages(response2.wsgi_request))
        self.assertIn(_('Label succesfully deleted'), messsages)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 302)
        self.assertRedirects(response2, reverse('label_list'))
        with self.assertRaises(ObjectDoesNotExist):
            Label.objects.get(name='label1')
