from django.test import TestCase
from app.models import Table

class ModelTestCase(TestCase):

  def setUp(self):
    table = Table.objects.create(name = 'Table #2')

  def test_table(self):
    table = Table.objects.get(name = 'Table #2')
    self.assertEqual(table.name, 'Table #2')