from django.test import TestCase

class TestUrl(TestCase):
    def testhomeurl(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code, 200)
