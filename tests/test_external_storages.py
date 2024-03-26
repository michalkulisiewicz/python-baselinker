import unittest
from unittest.mock import MagicMock

from baselinker.external_storages import ExternalStorages


class TestExternalStorages(unittest.TestCase):

    def setUp(self):
        self.mock_request = MagicMock()
        self.external_storages = ExternalStorages(api_token="my_token")
        self.external_storages.request = self.mock_request

    def test_get_external_storages_list(self):
        expected_params = {}
        self.mock_request.make_request.return_value = {'success': True, 'data': {'external_storages': []}}
        result = self.external_storages.get_external_storages_list()
        self.mock_request.make_request.assert_called_with('getExternalStoragesList', **expected_params)
        self.assertTrue(result['success'])

    def test_get_external_storage_categories(self):
        expected_params = {'storage_id': 'shop_123'}
        self.mock_request.make_request.return_value = {'success': True, 'data': {'categories': []}}
        result = self.external_storages.get_external_storage_categories(storage_id='shop_123')
        self.mock_request.make_request.assert_called_with('getExternalStorageCategories', **expected_params)
        self.assertTrue(result['success'])

    def test_get_external_storage_products_data(self):
        expected_params = {'storage_id': 'shop_123', 'products': [1, 2, 3]}
        self.mock_request.make_request.return_value = {'success': True, 'data': {'products_data': []}}
        result = self.external_storages.get_external_storage_products_data(storage_id='shop_123', products=[1, 2, 3])
        self.mock_request.make_request.assert_called_with('getExternalStorageProductsData', **expected_params)
        self.assertTrue(result['success'])

    def test_get_external_storage_products_list(self):
        expected_params = {
            'storage_id': 'shop_123',
            'filter_category_id': 'category_1',
            'filter_sort': None,
            'filter_id': None,
            'filter_ean': None,
            'filter_sku': None,
            'filter_name': None,
            'filter_price_from': None,
            'filter_price_to': None,
            'filter_quantity_from': None,
            'filter_quantity_to': None,
            'filter_available': None,
            'page': 1
        }
        self.mock_request.make_request.return_value = {'success': True, 'data': {'products_list': []}}
        result = self.external_storages.get_external_storage_products_list(
            storage_id='shop_123', filter_category_id='category_1', page=1
        )
        self.mock_request.make_request.assert_called_with('getExternalStorageProductsList', **expected_params)
        self.assertTrue(result['success'])

    def test_get_external_storage_products_quantity(self):
        expected_params = {'storage_id': 'shop_123', 'page': 1}
        self.mock_request.make_request.return_value = {'success': True, 'data': {'products_quantity': []}}
        result = self.external_storages.get_external_storage_products_quantity(storage_id='shop_123', page=1)
        self.mock_request.make_request.assert_called_with('getExternalStorageProductsQuantity', **expected_params)
        self.assertTrue(result['success'])

    def test_get_external_storage_products_prices(self):
        expected_params = {'storage_id': 'shop_123', 'page': 1}
        self.mock_request.make_request.return_value = {'success': True, 'data': {'products_prices': []}}
        result = self.external_storages.get_external_storage_products_prices(storage_id='shop_123', page=1)
        self.mock_request.make_request.assert_called_with('getExternalStorageProductsPrices', **expected_params)
        self.assertTrue(result['success'])

    def test_update_external_storage_products_quantity(self):
        expected_params = {'storage_id': 'shop_123', 'products': [[1, 0, 10], [2, 0, 20]]}
        self.mock_request.make_request.return_value = {'success': True, 'data': {'update_result': []}}
        result = self.external_storages.update_external_storage_products_quantity(
            storage_id='shop_123', products=[[1, 0, 10], [2, 0, 20]]
        )
        self.mock_request.make_request.assert_called_with('updateExternalStorageProductsQuantity', **expected_params)
        self.assertTrue(result['success'])
