from django.test import TestCase
from django.urls import reverse
from .models import SiteUser

# Create your tests here.
class TestUSers(TestCase):

    def setUp(self):
        self.test_user1 = SiteUser.objects.create_user(username='testuser1', password='12345')
        self.test_user1.save()
        
    def test_user_create_view(self):
        url = reverse('register')
        response1 = self.client.get(url)
        data = {'first_name': 'Perrito',
                'last_name': 'jobs',
                'username': 'testuser',
                'password1': '1234',
                'password2': '1234'}
        response2 = self.client.post(url, data)
        users = SiteUser.objects.filter(username='testuser')
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 302)
        self.assertRedirects(response2, '/login/')
        self.assertEqual(users.count(), 1)

    def test_user_update_view(self):
        user = self.test_user1
        self.client.force_login(user)
        url = reverse('user_update', args=(1,))
        response1 = self.client.get(url)
        data = {'first_name': 'Perrito',
                'last_name': 'jobs',
                'username': 'testuser2',
                'password1': '1234',
                'password2': '1234'}
        response2 = self.client.post(url, data)
        users = SiteUser.objects.filter(username='testuser2')
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 302)
        self.assertRedirects(response2, '/users/')
        self.assertEqual(users.count(), 1)

    def test_user_delete_view(self):
        user = self.test_user1
        self.client.force_login(user)
        url = reverse('user_delete', args=(1,))
        response1 = self.client.get(url)
        response2 = self.client.post(url)
        users = SiteUser.objects.filter(username='testuser1')
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 302)
        self.assertRedirects(response2, '/users/')
        self.assertEqual(users.count(), 0)
