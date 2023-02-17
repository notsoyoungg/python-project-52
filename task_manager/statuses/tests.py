from django.test import TestCase
from django.urls import reverse
from .models import Statuses
from task_manager.users.models import SiteUser

# Create your tests here.
class TestStatuses(TestCase):

    def setUp(self):
        self.test_status = Statuses.objects.create(name='status1')
        self.test_status.save()
        self.test_user1 = SiteUser.objects.create_user(username='testuser1', password='12345')
        self.test_user1.save()
        
    def test_status_create_view(self):
        user = self.test_user1
        self.client.force_login(user)
        url = reverse('create_status')
        response1 = self.client.get(url)
        data = {'name': 'В работе'}
        response2 = self.client.post(url, data)
        status = Statuses.objects.filter(name='В работе')
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 302)
        self.assertRedirects(response2, reverse('statuses_list'))
        self.assertEqual(status.count(), 1)

    def test_status_update_view(self):
        user = self.test_user1
        self.client.force_login(user)
        url = reverse('status_update', args=(1,))
        response1 = self.client.get(url)
        data = {'name': 'Исполнено'}
        response2 = self.client.post(url, data)
        users = Statuses.objects.filter(name='Исполнено')
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 302)
        self.assertRedirects(response2, reverse('statuses_list'))
        self.assertEqual(users.count(), 1)

    def test_status_delete_view(self):
        status_id = self.test_status.pk 
        user = self.test_user1
        self.client.force_login(user)
        url = reverse('status_delete', args=(status_id,))
        response1 = self.client.get(url)
        response2 = self.client.post(url)
        users = Statuses.objects.filter(name='status1')
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 302)
        self.assertRedirects(response2, reverse('statuses_list'))
        self.assertEqual(users.count(), 0)
