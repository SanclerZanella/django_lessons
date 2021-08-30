from django.test import TestCase
from .models import Item


class Testmodels(TestCase):

    def test_done_default_to_false(self):
        item = Item.objects.create(name='Test todo item')
        self.assertFalse(item.done)
