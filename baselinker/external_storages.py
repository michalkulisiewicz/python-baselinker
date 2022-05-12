from .request import Request


class ExternalStorages:
    def __init__(self, api_token):
        self.api_token = api_token
        self.request = Request(self.api_token)

    def get_external_storages_list(self):
        """
            The method allows you to retrieve a list of available external storages (shops, wholesalers)
            that can be referenced via API.
        """
        return self.request.make_request('getExternalStoragesList')

    def get_external_storage_categories(self, storage_id):
        """
            The method allows you to retrieve a category list from an external storage (shop/wholesale)
            connected to BaseLinker.
        Keywords:
            storage_id varchar(30): (required) Storage ID in format "[type:shop|warehouse]_[id:int]" (e.g. "shop_2445").
        """
        return self.request.make_request('getExternalStorageCategories', storage_id=storage_id)

    def get_external_storage_products_data(self, storage_id, products):
        """
            The method allows you to retrieve a category list from an external storage (shop/wholesale)
            connected to BaseLinker.
        Keywords:
            storage_id varchar(30): (required) Storage ID in format "[type:shop|warehouse]_[id:int]" (e.g. "shop_2445").
            products array: (required) An array of product ID numbers to download
        """
        return self.request.make_request('getExternalStorageProductsData', storage_id=storage_id, products=products)

    def get_external_storage_products_list(self, storage_id, filter_category_id=None, filter_sort=None, filter_id=None,
                                           filter_ean=None, filter_sku=None, filter_name=None, filter_price_from=None,
                                           filter_price_to=None, filter_quantity_from=None, filter_quantity_to=None,
                                           filter_available=None, page=None):
        """
            The method allows you to retrieve a category list from an external storage (shop/wholesale)
            connected to BaseLinker.
        Keywords:
            storage_id varchar(30): (required) Storage ID in format "[type:shop|warehouse]_[id:int]" (e.g. "shop_2445").
            filter_category_id varchar(30): (optional) Retrieving products from a specific category
            filter_sort	 varchar(30): (optional) the value for sorting the product list.
            Possible values: "id [ASC|DESC]", "name [ASC|DESC]", "quantity [ASC|DESC]", "price [ASC|DESC]"
            filter_id varchar(30): (optional) limiting results to a specific product id
            filter_ean varchar(320): (optional) limiting results to a specific ean
            filter_sku varchar(32): (optional) limiting the results to a specific SKU (stock keeping number)
            filter_name varchar(100): (optional) item name filter (part of the searched name or an empty field)
            filter_price_from (float): (optional) minimum price limit (not displaying products with lower price)
            filter_price_to (float): (optional) maximum price limit
            filter_quantity_from (int): (optional) maximum price limit
            filter_quantity_to (int): (optional) maximum quantity limit
            filter_available (int): (optional) displaying only products marked as available (value 1) or not available (0) or all (empty value)
            page (int): (optional) pagination
        """
        return self.request.make_request('getExternalStorageProductsList', storage_id=storage_id,
                                         filter_category_id=filter_category_id,
                                         filter_sort=filter_sort, filter_id=filter_id, filter_ean=filter_ean,
                                         filter_sku=filter_sku, filter_name=filter_name,
                                         filter_price_from=filter_price_from,
                                         filter_price_to=filter_price_to, filter_quantity_from=filter_quantity_from,
                                         filter_quantity_to=filter_quantity_to, filter_available=filter_available,
                                         page=page)

    def get_external_storage_products_quantity(self, storage_id, page):
        """
            The method allows you to retrieve a category list from an external storage (shop/wholesale)
            connected to BaseLinker.
        Keywords:
            storage_id varchar(30): (required) Storage ID in format "[type:shop|warehouse]_[id:int]" (e.g. "shop_2445").
            page (int): (optional) pagination
        """
        return self.request.make_request('getExternalStorageProductsQuantity', storage_id=storage_id, page=page)

    def get_external_storage_products_prices(self, storage_id, page):
        """
            The method allows you to retrieve a category list from an external storage (shop/wholesale)
            connected to BaseLinker.
        Keywords:
            storage_id varchar(30): (required) Storage ID in format "[type:shop|warehouse]_[id:int]" (e.g. "shop_2445").
            page (int): (optional) pagination
        """
        return self.request.make_request('getExternalStorageProductsPrices', storage_id=storage_id, page=page)

    def update_external_storage_products_quantity(self, storage_id, products):
        """
            The method allows to bulk update the product stock (and/or variants) in an external storage (shop/wholesaler)
            connected to BaseLinker. Maximum 1000 products at a time.
        Keywords:
            storage_id varchar(30): (required) Storage ID in format "[type:shop|warehouse]_[id:int]" (e.g. "shop_2445").
            products array: (required) An array of products. Each product is a separate element of the array.
            The product consists of a 3 element array of components:
            0 => product ID number (varchar)
            1 => variant ID number (0 if the main product is changed, not the variant) (int)
            2 => Stock quantity (int)
        """
        return self.request.make_request('updateExternalStorageProductsQuantity', storage_id=storage_id,
                                         products=products)