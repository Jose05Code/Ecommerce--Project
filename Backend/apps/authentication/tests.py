from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class AuthenticationTestCase(TestCase):

    def setUp(self):
        self.client = self.client
        self.data = {
            "username": 'test',
            "password": 'test123',
            "email": 'test@gmail.com'
        }

    def test_register(self):
        url = reverse('register')
        # send a post request to the url with the data
        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, 201)
        
        user_count = User.objects.filter(username='test').count()
        self.assertEqual(user_count, 1)

        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, 400)
        
        user_count = User.objects.filter(username='test').count()
        self.assertEqual(user_count, 1)

    def test_login(self):
        url = reverse('login')
        User.objects.create_user(**self.data)
        
        # send a post request to the url with the data
        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, 200)

        response_data = response.json()
        self.assertIn(self.data['username'], response_data['username'])

        self.data['password'] = 'wrong_password'

        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, 400)

        


