
from django.test import TestCase
from restaurant.models import menu


class MenuModelTest(TestCase):
    def test_get_menu(self):
        item = menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.title, "IceCream")  # Assert equality for title
        self.assertEqual(item.price, 80)