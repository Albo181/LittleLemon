
from django.test import TestCase
from django.urls import reverse
from restaurant.models import menu
from restaurant.views import MenuItemView
from django.core.serializers import serialize

class MenuViewtest(TestCase):
    def setUp(self):
        menu.objects.create(title="IceCream", price=80, inventory=100)
        menu.objects.create(title="Cake", price=120, inventory=50)
        menu.objects.create(title="Coffee", price=35, inventory=200)

    def test_getall(self):
        response = self.client.get(reverse("menu_item"))
        menus = menu.objects.all()
        serialized_data = serialize("json", menus)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, serialized_data)





