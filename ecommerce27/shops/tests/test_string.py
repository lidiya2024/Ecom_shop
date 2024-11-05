from django.test import TestCase

def demo(txt1,txt2):
    return txt1 + txt2
class TestDemo(TestCase):
    def test_concatenate(self):
        self.assertEqual(demo("Python"," Program"), "Python Program")

