from django.http import response
from django.test import TestCase

# Create your tests here.

class URL_Tester(TestCase):
    def test_homepage_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)