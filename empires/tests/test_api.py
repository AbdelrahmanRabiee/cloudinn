from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase

from empires.models import Unit


class TestUnitAPI(APITestCase):
    def setUp(self):
        self.search_url = '/api/v1/unit/?search='

        mommy.make(Unit, name='Eagle Warrior', age='Castle', _quantity=5)
        mommy.make(Unit, name='Spearman', age='Feudal', _quantity=5)


    def test_user_can_seach_with_unit_name(self):
        """check that user can search by unit name and get result"""
        resp = self.client.get(self.search_url+'Spearman')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['count'], 5)

    def test_user_can_seach_with_unit_age(self):
        """check that user can search by unit age and get result"""
        resp = self.client.get(self.search_url+'Castle')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['count'], 5)      
