from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
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
        self.assertIn('token', response_data)

        self.data['password'] = 'wrong_password'

        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, 400)

    def test_logout(self):
        url = reverse('logout')
        user = User.objects.create_user(**self.data)
        self.client.login(username='test', password='test123')
        token = Token.objects.create(user=user)
        api_client = APIClient()
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        url = reverse('logout')

        # Send a post request to the url
        response = api_client.post(url)
        self.assertEqual(response.status_code, 200)

        # Check that the token was deleted
        exists = Token.objects.filter(user=user).exists()
        self.assertFalse(exists)
            


