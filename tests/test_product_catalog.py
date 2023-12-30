import unittest
from unittest.mock import MagicMock
from baselinker.product_catalog import ProductCatalog


class TestProductCatalog(unittest.TestCase):

    def setUp(self):
        self.mock_request = MagicMock()
        self.product_catalog = ProductCatalog(api_token="my_token")
        self.product_catalog.request = self.mock_request

    def test_add_inventory_price_group(self):
        expected_params = {'price_group_id': 1, 'name': 'Test Group', 'description': 'Test Description',
                           'currency': 'USD'}
        self.mock_request.make_request.return_value = {'success': True, 'data': {}}
        result = self.product_catalog.add_inventory_price_group(price_group_id=1, name='Test Group',
                                                                description='Test Description', currency='USD')
        self.mock_request.make_request.assert_called_with('addInventoryPriceGroup', **expected_params)
        self.assertTrue(result['success'])

    def test_delete_inventory_price_group(self):
        expected_params = {'price_group_id': 1}
        self.mock_request.make_request.return_value = {'success': True, 'data': {}}
        result = self.product_catalog.delete_inventory_price_group(price_group_id=1)
        self.mock_request.make_request.assert_called_with('deleteInventoryPriceGroup', **expected_params)
        self.assertTrue(result['success'])

    def test_get_inventory_price_groups(self):
        self.mock_request.make_request.return_value = {'success': True, 'data': {'price_groups': []}}
        result = self.product_catalog.get_inventory_price_groups()
        self.mock_request.make_request.assert_called_with('getInventoryPriceGroups')
        self.assertTrue(result['success'])

    def test_add_inventory_warehouse(self):
        expected_params = {'warehouse_id': 1, 'name': 'Test Warehouse', 'description': 'Test Description',
                           'stock_edition': True}
        self.mock_request.make_request.return_value = {'success': True, 'data': {}}
        result = self.product_catalog.add_inventory_warehouse(warehouse_id=1, name='Test Warehouse',
                                                              description='Test Description', stock_edition=True)
        self.mock_request.make_request.assert_called_with('addInventoryWarehouse', **expected_params)
        self.assertTrue(result['success'])

    def test_delete_inventory_warehouse(self):
        expected_params = {'warehouse_id': 1}
        self.mock_request.make_request.return_value = {'success': True, 'data': {}}
        result = self.product_catalog.delete_inventory_warehouse(warehouse_id=1)
        self.mock_request.make_request.assert_called_with('deleteInventoryWarehouse', **expected_params)
        self.assertTrue(result['success'])

    def test_get_inventory_warehouses(self):
        self.mock_request.make_request.return_value = {'success': True, 'data': {'warehouses': []}}
        result = self.product_catalog.get_inventory_warehouses()
        self.mock_request.make_request.assert_called_with('getInventoryWarehouses')
        self.assertTrue(result['success'])

    def test_add_inventory(self):
        inventory_id = 1
        name = "Test Catalog"
        description = "Test Catalog Description"
        languages = ["en", "pl"]
        default_language = "en"
        price_groups = [1, 2]
        default_price_group = 1
        warehouses = ["shop_1", "warehouse_2"]
        default_warehouse = "shop_1"
        reservations = True

        self.product_catalog.add_inventory(
            inventory_id=inventory_id,
            name=name,
            description=description,
            languages=languages,
            default_language=default_language,
            price_groups=price_groups,
            default_price_group=default_price_group,
            warehouses=warehouses,
            default_warehouse=default_warehouse,
            reservations=reservations
        )

        self.mock_request.make_request.assert_called_once_with(
            'addInventory',
            inventory_id=inventory_id,
            name=name,
            description=description,
            languages=languages,
            default_language=default_language,
            price_groups=price_groups,
            default_price_group=default_price_group,
            warehouses=warehouses,
            default_warehouse=default_warehouse,
            reservations=reservations
        )

    def test_delete_inventory(self):
        inventory_id = 1

        self.product_catalog.delete_inventory(inventory_id=inventory_id)

        self.mock_request.make_request.assert_called_once_with(
            'deleteInventory',
            inventory_id=inventory_id
        )

    def test_get_inventories(self):
        self.product_catalog.get_inventories()

        self.mock_request.make_request.assert_called_once_with('getInventories')

    def test_add_inventory_category(self):
        inventory_id = 1
        category_id = 2
        name = "Test Category"
        parent_id = 0

        self.product_catalog.add_inventory_category(
            inventory_id=inventory_id,
            category_id=category_id,
            name=name,
            parent_id=parent_id
        )

        self.mock_request.make_request.assert_called_once_with(
            'addInventoryCategory',
            inventory_id=inventory_id,
            category_id=category_id,
            name=name,
            parent_id=parent_id
        )

    def test_delete_inventory_category(self):
        category_id = 1

        self.product_catalog.delete_inventory_category(category_id=category_id)

        self.mock_request.make_request.assert_called_once_with(
            'deleteInventoryCategory',
            category_id=category_id
        )

    def test_get_inventory_categories(self):
        inventory_id = 1

        self.product_catalog.get_inventory_categories(inventory_id=inventory_id)

        self.mock_request.make_request.assert_called_once_with(
            'getInventoryCategories',
            inventory_id=inventory_id
        )

    def test_add_inventory_manufacturer(self):
        manufacturer_id = 1
        name = "Test Manufacturer"

        self.product_catalog.add_inventory_manufacturer(
            manufacturer_id=manufacturer_id,
            name=name
        )

        self.mock_request.make_request.assert_called_once_with(
            'addInventoryManufacturer',
            manufacturer_id=manufacturer_id,
            name=name
        )

    def test_delete_inventory_manufacturer(self):
        manufacturer_id = 1

        self.product_catalog.delete_inventory_manufacturer(manufacturer_id=manufacturer_id)

        self.mock_request.make_request.assert_called_once_with(
            'deleteInventoryManufacturer',
            manufacturer_id=manufacturer_id
        )

    def test_get_inventory_manufacturers(self):
        self.product_catalog.get_inventory_manufacturers()

        self.mock_request.make_request.assert_called_once_with('getInventoryManufacturers')

    def test_get_inventory_extra_fields(self):
        self.mock_request.make_request.return_value = {'success': True, 'data': {'extra_fields': []}}
        result = self.product_catalog.get_inventory_extra_fields()
        self.mock_request.make_request.assert_called_with('getInventoryExtraFields')
        self.assertTrue(result['success'])

    def test_get_inventory_integrations(self):
        self.mock_request.make_request.return_value = {'success': True, 'data': {'integrations': []}}
        result = self.product_catalog.get_inventory_integrations(inventory_id=1)
        self.mock_request.make_request.assert_called_with('getInventoryIntegrations', inventory_id=1)
        self.assertTrue(result['success'])

    def test_get_inventory_available_text_field_keys(self):
        self.mock_request.make_request.return_value = {'success': True, 'data': {'text_field_keys': []}}
        result = self.product_catalog.get_inventory_available_text_field_keys(inventory_id=1)
        self.mock_request.make_request.assert_called_with('getInventoryAvailableTextFieldKeys', inventory_id=1)
        self.assertTrue(result['success'])

    def test_add_inventory_product(self):
        expected_params = {'inventory_id': 1, 'product_id': 2, 'parent_id': 0, 'is_bundle': False,
                           'ean': '1234567890123', 'sku': 'TEST123', 'tax_rate': 20.0, 'weight': 1.5,
                           'height': 10.0, 'width': 5.0, 'length': 8.0, 'star': 4, 'manufacturer_id': 3,
                           'category_id': 4, 'prices': {1: 100.0, 2: 90.0}, 'stock': {'bl_1': 50, 'shop_2': 30},
                           'locations': {'bl_1': 'A-5-2', 'shop_2': 'B-3-1'}, 'text_fields': {'name': 'Test Product'},
                           'images': ['url:http://example.com/image.jpg'], 'links': ['shop_2_123'],
                           'bundle_products': {}}
        self.mock_request.make_request.return_value = {'success': True, 'data': {}}
        result = self.product_catalog.add_inventory_product(inventory_id=1, product_id=2, parent_id=0, is_bundle=False,
                                                            ean='1234567890123', sku='TEST123', tax_rate=20.0,
                                                            weight=1.5, height=10.0, width=5.0, length=8.0, star=4,
                                                            manufacturer_id=3, category_id=4,
                                                            prices={1: 100.0, 2: 90.0},
                                                            stock={'bl_1': 50, 'shop_2': 30},
                                                            locations={'bl_1': 'A-5-2', 'shop_2': 'B-3-1'},
                                                            text_fields={'name': 'Test Product'},
                                                            images=['url:http://example.com/image.jpg'],
                                                            links=['shop_2_123'], bundle_products={})
        self.mock_request.make_request.assert_called_with('addInventoryProduct', **expected_params)
        self.assertTrue(result['success'])

    def test_delete_inventory_product(self):
        expected_params = {'product_id': 1}
        self.mock_request.make_request.return_value = {'success': True, 'data': {}}
        result = self.product_catalog.delete_inventory_product(product_id=1)
        self.mock_request.make_request.assert_called_with('deleteInventoryProduct', **expected_params)
        self.assertTrue(result['success'])

    def test_get_inventory_products_data(self):
        expected_params = {'inventory_id': 1, 'products': [1, 2, 3]}
        self.mock_request.make_request.return_value = {'success': True, 'data': {'products_data': []}}
        result = self.product_catalog.get_inventory_products_data(inventory_id=1, products=[1, 2, 3])
        self.mock_request.make_request.assert_called_with('getInventoryProductsData', **expected_params)
        self.assertTrue(result['success'])

    def test_get_inventory_products_list(self):
        expected_params = {'inventory_id': 1, 'filter_id': 2, 'filter_category_id': 3, 'filter_ean': '1234567890123',
                           'filter_sku': 'TEST123', 'filter_name': 'Test', 'filter_price_from': 50.0,
                           'filter_stock_from': 20, 'filter_price_to': 100.0, 'page': 1, 'filter_sort': 'id ASC'}
        self.mock_request.make_request.return_value = {'success': True, 'data': {'products_list': []}}
        result = self.product_catalog.get_inventory_products_list(inventory_id=1, filter_id=2, filter_category_id=3,
                                                                  filter_ean='1234567890123', filter_sku='TEST123',
                                                                  filter_name='Test', filter_price_from=50.0,
                                                                  filter_stock_from=20, filter_price_to=100.0,
                                                                  page=1, filter_sort='id ASC')
        self.mock_request.make_request.assert_called_with('getInventoryProductsList', **expected_params)
        self.assertTrue(result['success'])

    def test_get_inventory_products_stock(self):
        expected_params = {'inventory_id': 1, 'page': 1}
        self.mock_request.make_request.return_value = {'success': True, 'data': {'products_stock': []}}
        result = self.product_catalog.get_inventory_products_stock(inventory_id=1, page=1)
        self.mock_request.make_request.assert_called_with('getInventoryProductsStock', **expected_params)
        self.assertTrue(result['success'])

    def test_update_inventory_products_stock(self):
        expected_params = {'inventory_id': 1,
                           'products': {1: {'bl_1': 50, 'shop_2': 30}, 2: {'bl_1': 20, 'shop_2': 10}}}
        self.mock_request.make_request.return_value = {'success': True, 'data': {}}
        result = self.product_catalog.update_inventory_products_stock(inventory_id=1,
                                                                      products={1: {'bl_1': 50, 'shop_2': 30},
                                                                                2: {'bl_1': 20, 'shop_2': 10}})
        self.mock_request.make_request.assert_called_with('updateInventoryProductsStock', **expected_params)
        self.assertTrue(result['success'])

    def test_get_inventory_products_prices(self):
        expected_params = {'inventory_id': 1, 'page': 1}
        self.mock_request.make_request.return_value = {'success': True, 'data': {'products_prices': []}}
        result = self.product_catalog.get_inventory_products_prices(inventory_id=1, page=1)
        self.mock_request.make_request.assert_called_with('getInventoryProductsPrices', **expected_params)
        self.assertTrue(result['success'])

    def test_update_inventory_products_prices(self):
        expected_params = {'inventory_id': 1, 'products': {1: {1: 100.0, 2: 90.0}, 2: {1: 80.0, 2: 70.0}}}
        self.mock_request.make_request.return_value = {'success': True, 'data': {}}
        result = self.product_catalog.update_inventory_products_prices(inventory_id=1,
                                                                       products={1: {1: 100.0, 2: 90.0},
                                                                                 2: {1: 80.0, 2: 70.0}})
        self.mock_request.make_request.assert_called_with('updateInventoryProductsPrices', **expected_params)
        self.assertTrue(result['success'])

    def test_get_inventory_product_logs(self):
        expected_params = {'product_id': 1, 'date_from': 1640908800, 'date_to': 1640995199, 'log_type': 1,
                           'sort': 'ASC', 'page': 1}
        self.mock_request.make_request.return_value = {'success': True, 'data': {'product_logs': []}}
        result = self.product_catalog.get_inventory_product_logs(product_id=1, date_from=1640908800, date_to=1640995199,
                                                                 log_type=1, sort='ASC', page=1)
        self.mock_request.make_request.assert_called_with('getInventoryProductLogs', **expected_params)
        self.assertTrue(result['success'])
