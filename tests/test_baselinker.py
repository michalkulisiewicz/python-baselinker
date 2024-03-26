import unittest
from unittest.mock import MagicMock
from baselinker import Baselinker


class TestBaselinker(unittest.TestCase):
    def setUp(self):
        self.request_mock = MagicMock()
        self.orders_mock = MagicMock()
        self.external_storages_mock = MagicMock()
        self.product_catalog_mock = MagicMock()

        self.baselinker = Baselinker(api_token='my_token')
        self.baselinker.request = self.request_mock
        self.baselinker.orders = self.orders_mock
        self.baselinker.external_storages = self.external_storages_mock
        self.baselinker.product_catalog = self.product_catalog_mock

    def test_baselinker_initialization(self):
        self.assertEqual(self.baselinker.api_token, 'my_token')
        self.assertIsInstance(self.baselinker.request, MagicMock)
        self.assertIsInstance(self.baselinker.orders, MagicMock)
        self.assertIsInstance(self.baselinker.external_storages, MagicMock)
        self.assertIsInstance(self.baselinker.product_catalog, MagicMock)
