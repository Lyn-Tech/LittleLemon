from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
    
    def test_title(self):
        menu = Menu.objects.get(id=1)
        field_label = menu._meta.get_field('title').verbose_name
        self.assertEqual(field_label,'title')
    
    def test_price(self):
        menu = Menu.objects.get(id=1)
        field_label = menu._meta.get_field('price').verbose_name
        self.assertEqual(field_label,'price')
        