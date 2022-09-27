from rest_framework import response, status
from rest_framework.test import APITestCase
from django.urls import reverse


class TestListCreateTodos(APITestCase):

    def authenticate(self):
        self.client.post(reverse('admin_register'), {

            "username": "fiha111@gmail.com",
            "email":"fiha111@gmail.com",
            "password":"123456"
        })

        response=self.client.post(reverse('login'),{

            "username": "fiha111@gmail.com",
            "password":"123456"
        })
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['token']}")
    def test_creates_todo(self):
        self.authenticate()
        self.client.get(reverse('weather_type'))
        sample_data = {
            "name": "Summer",
            "high_value": 40.0,
            "low_value": 30.0
        }
        self.client.post(reverse('weather_type'), sample_data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
