from .request import Request


class ProductCatalog:
    def __init__(self, api_token):
        self.api_token = api_token
        self.request = Request(self.api_token)


    def add_inventory_price_group(self, price_group_id, name, description, currency):
        """
            The method allows to create a price group in BaseLinker storage.
            Providing a price group ID will update the existing price group.
            Such price groups may be later assigned in addInventory method.
        Keywords:
            price_group_id int: (required) Price group identifier
            name varchar(100): (required) Name of the price group
            description text: (required) Price group description
            currency char(3): (required) 3-letter currency symbol e.g. PLN, EUR
        """
        return self.request.make_request('addInventoryPriceGroup', price_group_id=price_group_id, name=name,
                                         description=description, currency=currency)


    def delete_inventory_price_group(self, price_group_id):
        """
            The method allows you to remove the price group from BaseLinker storage.
        Keywords:
            price_group_id int: (required) Price group identifier
        """
        return self.request.make_request('deleteInventoryPriceGroup', price_group_id=price_group_id)


    def get_inventory_price_groups(self):
        """
            The method allows to retrieve price groups existing in BaseLinker storage
        """
        return self.request.make_request('getInventoryPriceGroups')


    def add_inventory_warehouse(self, warehouse_id, name, description, stock_edition):
        """
            The method allows you to add a new warehouse available in BaseLinker catalogues.
            Adding a warehouse with the same identifier again will cause updates of the previously saved warehouse.
            The method does not allow editing warehouses created automatically
            for the purpose of keeping external stocks of shops,
            wholesalers etc. Such warehouse may be later used in addInventory method.
        Keywords:
            warehouse_id int: (required) ID of the warehouse
            name varchar(100): (required) Warehouse name
            description text: (required) Warehouse description
            stock_edition bool: (required) Is manual editing of stocks permitted.
            A false value means that you can only edit your stock through the API.
        """
        return self.request.make_request('addInventoryWarehouse', warehouse_id=warehouse_id, name=name,
                                         description=description, stock_edition=stock_edition)


    def delete_inventory_warehouse(self, warehouse_id):
        """
           The method allows you to remove the warehouse available in BaseLinker catalogues.
           The method does not allow to remove warehouses created automatically
           for the purpose of keeping external stocks of shops, wholesalers etc.
        Keywords:
            warehouse_id int: (required) ID of the warehouse
        """
        return self.request.make_request('deleteInventoryWarehouse', warehouse_id=warehouse_id)


    def get_inventory_warehouses(self):
        """
            The method allows you to retrieve a list of warehouses available in BaseLinker catalogues.
            The method also returns information about the warehouses created automatically
            for the purpose of keeping external stocks (shops, wholesalers etc.)
        """
        return self.request.make_request('getInventoryWarehouses')


    def add_inventory(self, inventory_id, name, description, languages, default_language, price_groups,
                      default_price_group, warehouses, default_warehouse, reservations):
        """
           The method allows you to add the BaseLinker catalogs.
           Adding a catalog with the same identifier again will cause updates of the previously saved catalog.
        Keywords:
            inventory_id int: (required) Catalog ID. The list of identifiers can be retrieved using the method get_inventories.
            name varchar(100): (required) Catalog name
            description text: (required) Catalog description
            languages array: (required) An array of languages available in the catalogue.
            default_language char(2): (required) Default catalogue language. Must be included in the "languages" parameter.
            price_groups (array): (required) An array of price group identifiers available in the catalogue.
            The list of price group identifiers can be downloaded using the get_inventory_price_groups method
            default_price_group	 int: (required) ID of the price group default for the catalogue.
            The identifier must be included in the "price_groups" parameter.
            warehouses (array): (required) An array of warehouse identifiers available in the catalogue.
            The list of warehouse identifiers can be retrieved using the get_inventory_warehouses API method.
            The format of the identifier should be as follows: "[type:bl|shop|warehouse]_[id:int]". (e.g. "shop_2445")
            default_warehouse varchar(30): (required) Identifier of the warehouse default for the catalogue.
            The identifier must be included in the "warehouses" parameter.
            reservations (bool): (required) Does this catalogue support reservations
        """
        return self.request.make_request('addInventory', inventory_id=inventory_id, name=name,
                                         description=description, languages=languages,
                                         default_language=default_language, price_groups=price_groups,
                                         default_price_group=default_price_group, warehouses=warehouses,
                                         default_warehouse=default_warehouse, reservations=reservations)


    def delete_inventory(self, inventory_id):
        """
            The method allows you to delete a catalog from BaseLinker storage.
        Keywords:
            inventory_id int: (required) Catalog ID. The list of identifiers can be retrieved using the method get_inventories.
        """
        return self.request.make_request('deleteInventory', inventory_id=inventory_id)


    def get_inventories(self):
        """
            The method allows you to retrieve a list of catalogs available in the BaseLinker storage.
        """
        return self.request.make_request('getInventories')


    def add_inventory_category(self, inventory_id, category_id, name, parent_id):
        """
            The method allows you to add a category to the BaseLinker catalog.
            Adding a category with the same identifier again, updates the previously saved category
        Keywords:
            inventory_id int: (required) Catalog ID. The list of identifiers can be retrieved using the method get_inventories.
            category_id int: (required) The category identifier to be provided for updates. Should be left blank when creating a new category.
            name varchar(200): (required) Category name
            parent_id int: (required) The parent category identifier obtained previously at the output of the
            add_category method. Categories should be added starting from the hierarchy root so that
            the child is always added after the parent (you need to know the parent ID to add the child).
            For the top level category, 0 should be given as parent_id.
        """
        return self.request.make_request('addInventoryCategory', inventory_id=inventory_id, category_id=category_id,
                                         name=name, parent_id=parent_id)


    def delete_inventory_category(self, category_id):
        """
            The method allows you to remove categories from BaseLinker warehouse.
            Along with the category, the products contained therein are removed
            (however, this does not apply to products in subcategories).
            The subcategories will be changed to the highest level categories.
        Keywords:
            category_id int: (required) The number of the category to be removed in the BaseLinker storage.
        """
        return self.request.make_request('deleteInventoryCategory', category_id=category_id)


    def get_inventory_categories(self, inventory_id):
        """
            The method allows you to retrieve a list of categories for a BaseLinker catalog.
        Keywords:
            inventory_id int: (required) Catalog ID. The list of identifiers can be retrieved by
            the get_inventories method (inventory_id field).
            To retrieve categories available for all catalogs created in BaseLinker, this field should be omitted.
        """
        return self.request.make_request('getInventoryCategories', inventory_id=inventory_id)


    def add_inventory_manufacturer(self, manufacturer_id, name):
        """
            The method allows you to retrieve a list of categories for a BaseLinker catalog.
        Keywords:
            manufacturer_id int: (required) Manufacturer ID provided in case of an update. Should be blank when creating a new manufacturer.
            name varchar(200): (required) Manufacturer name
        """
        return self.request.make_request('addInventoryManufacturer', manufacturer_id=manufacturer_id, name=name)


    def delete_inventory_manufacturer(self, manufacturer_id):
        """
            The method allows you to remove manufacturer from BaseLinker catalog
        Keywords:
            manufacturer_id int: (required) The ID of the manufacturer removed from BaseLinker warehouse.
        """
        return self.request.make_request('deleteInventoryManufacturer', manufacturer_id=manufacturer_id)


    def get_inventory_manufacturers(self):
        """
            The method allows you to retrieve a list of manufacturers for a BaseLinker catalog.
        """
        return self.request.make_request('getInventoryManufacturers')


    def get_inventory_extra_fields(self):
        """
            The method allows you to retrieve a list of extra fields for a BaseLinker catalog.
        """
        return self.request.make_request('getInventoryExtraFields')


    def get_inventory_integrations(self, inventory_id):
        """
            The method returns a list of integrations where text values in the catalog can be overwritten.
            The returned data contains a list of accounts for each integration
            and a list of languages supported by the integration
        Keywords:
            inventory_id int: (required) Catalog ID.
            The list of identifiers can be retrieved using the method get_inventories. (inventory_id field).
        """
        return self.request.make_request('getInventoryIntegrations', inventory_id=inventory_id)


    def get_inventory_available_text_field_keys(self, inventory_id):
        """
            The method returns a list of product text fields that can be overwritten for specific integration.
        Keywords:
            inventory_id int: (required) Catalog ID. The list of identifiers can be retrieved
            by the get_inventories method (inventory_id field).
        """
        return self.request.make_request('getInventoryAvailableTextFieldKeys', inventory_id=inventory_id)


    def add_inventory_product(self, inventory_id, product_id, parent_id, is_bundle, ean,
                              sku, tax_rate, weight, height, width, length, star,
                              manufacturer_id, category_id, prices, stock, locations,
                              text_fields, images, links, bundle_products):
        """
            The method allows you to add a new product to BaseLinker catalog. Entering the product with the ID updates previously saved product.
        Keywords:
            inventory_id	varchar(30)	Catalog ID. The list of identifiers can be retrieved using the method getInventories. (inventory_id field).
            product_id	varchar(30)	Main product identifier, given only during the update. Should be left blank when creating a new product. The new product identifier is returned as a response to this method.
            parent_id	varchar(30)	Product parent ID. To be provided only if the added/edited product is a variant of another product.
            is_bundle	bool	Is the given product a part of a bundle
            ean	varchar(32)	Product EAN number.
            sku	varchar(50)	Product SKU number.
            tax_rate	float	VAT tax rate (e.g. "20")
            weight	decimal(10,2)	Weight in kilograms.
            height	decimal(10,2)	Product height
            width	decimal(10,2)	Product width
            length	decimal(10,2)	Product length
            star	int	Product star type. It takes from 0 to 5 values. 0 means no starring.
            manufacturer_id	int	Product manufacturer ID. IDs can be retrieved with getInventoryManufacturers method.
            category_id	int	Product category ID (category must be previously created with addInventoryCategories) method.
            prices	array	A list containing product prices, where the key is the price group ID
            and value is a product gross price for a given price group.
            The list of price groups can be retrieved with get_inventory_price_groups method.
            locations array	A list containing product locations where the key is the warehouse ID and value is
            a product location for a given warehouse, eg. "A-5-2".
            Warehouse ID should have this format: "[type:bl|shop|warehouse]_[id:int]" (eg. "bl_123").
            The list of warehouse IDs can be retrieved with get_inventory_warehouses method.
            text_fields	array A list containing field text values (names, descriptions, etc.) of a product,
            where the key is the field text ID and value is the field value.
            The field text ID consists of the following components separated with the "|" character:
            [field] - Field name. Accepted field names: "name", "description", "features", "description_extra1", "description_extra2", "description_extra3", "description_extra4", "extra_field_[extra-field-ID]" e.g. "extra_field_75". The list of extra fields IDs can be retrieved with getInventoryExtraFields method.
            [lang] - A two-letter code of language, which gets assigned given value e.g. "en". If this value is not specified, the default catalog language is assigned. The list of languages available for each integration can be retrieved with getInventoryIntegrations method.
            [source_id] - Integration ID provided when the given text field value is to be overwritten only for a specific integration. ID should have a following format: "[type:varchar]_[id:int]", where the type means a kind of integration (e.g. "ebay", "amazon", "google"), and ID is an account identifier for given integration (eg. "ebay_2445").
            If a value is to be overwritten throughout the integration (e.g. for all Amazon accounts), the value "0" should be used as the identifier. (e.g. "amazon_0").
            Examples of text field identifiers:
            "name" - Default name assigned to the default language.
            "name|de" - Name assigned to a particular language.
            "name|de|amazon_0" - Name assigned to a specific language for all Amazon accounts.
            "name|de|amazon_123" - Name assigned to a specific language for an Amazon account with ID 123.
            The list of all text field identifiers can be retrieved with the getInventoryAvailableTextFieldKeys method.
            In the case of the name and short additional fields, the character limit for the field value is 200.
            When specifying the value of a product feature (field "features"),
            provide a list where the key is the name of the parameter (e.g. "Colour") and the value is the value of that parameter (e.g. "White").
            images	array	An array of product images (maximum 16). Each element of the array is a separate photo.
            You can submit a photo in binary format, or a link to the photo. In case of binary format,
            the photo should be coded in base64 and at the very beginning of the photo string the prefix "data:"
            should be provided. In case of link to the photo, the prefix "url:" must be given before the link.
            Example:
            images[0] = "url:http://adres.pl/zdjecie.jpg";
            images[1] = "data:4AAQSkZJRgABA[...]";
            links	array	An array containing product links to external warehouses (e.g. shops, wholesalers).
            Each element of the array is a list in which the key is the identifier of the external warehouse in the format:
            "[type:shop|warehouse]_[id:int]". (e.g. "shop_2445").
            The warehouse identifiers can be retrieved with the getStoragesList method. The value is an array containing the fields listed below.
                | - product_id	varchar	Product identifier in external warehouse.
                | - variant_id (optional)	varchar	Product variant identifier in the external warehouse.
                When assigning a link to a main product, this parameter shall be omitted or a value of 0 provided.
            bundle_products	array A list containing information about the products included in the bundle,
            where the key is the identifier of the product included in the bundle,
            and the value is the number of pieces of this product in the bundle.
            Subproducts can only be defined if the added/edited product is a bundle (is_bundle = true).
        """
        return self.request.make_request('addInventoryProduct', inventory_id=inventory_id, product_id=product_id,
                                         parent_id=parent_id, is_bundle=is_bundle, ean=ean,
                                         sku=sku, tax_rate=tax_rate, weight=weight, height=height,
                                         width=width, length=length, star=star, manufacturer_id=manufacturer_id
                                         , category_id=category_id, prices=prices, stock=stock, locations=locations,
                                         text_fields=text_fields, images=images, links=links,
                                         bundle_products=bundle_products)


    def delete_inventory_product(self, product_id):
        """
            The method allows you to remove the product from BaseLinker catalog.
        Keywords:
            product_id int: (required) BaseLinker catalogue product identifier
        """
        return self.request.make_request('deleteInventoryProduct', product_id=product_id)


    def get_inventory_products_data(self, inventory_id, products):
        """
            The method allows you to retrieve detailed data for selected products from the BaseLinker catalogue.
        Keywords:
            inventory_id int: (required) Catalog ID. The list of identifiers can be retrieved
            by the get_inventories method (inventory_id field).
            products array (required) An array of product ID numbers to download
        """
        return self.request.make_request('getInventoryProductsData', inventory_id=inventory_id, products=products)


    def get_inventory_products_list(self, inventory_id, filter_id=None, filter_category_id=None,
                                    filter_ean=None, filter_sku=None, filter_name=None, filter_price_from=None,
                                    filter_stock_from=None, filter_price_to=None, page=None, filter_sort=None):
        """
            The method allows to retrieve a basic data of chosen products from BaseLinker catalogs.

        Keywords:
            inventory_id int: (required) Catalog ID. The list of identifiers can be retrieved by the get_inventories method
            filter_id int (optional) limiting results to a specific product id
            filter_category_id int (optional) Retrieving products from a specific category
            filter_ean varchar(32) (optional) limiting results to a specific ean
            filter_sku varchar(50) (optional) limiting the results to a specific SKU (stock keeping number)
            filter_name varchar(200) (optional) item name filter (part of the searched name or an empty field)
            filter_price_from float (optional) minimum price limit (not displaying products with lower price)
            filter_price_to float (optional) maximum price limit
            filter_stock_from int (optional) minimum quantity limit
            page int (optional) Results paging (1000 products per page for BaseLinker warehouse)
            filter_sort varchar(30) (optional) the value for sorting the product list. Possible values: "id [ASC|DESC]"
        """
        return self.request.make_request('getInventoryProductsList', inventory_id=inventory_id, filter_id=filter_id,
                                         filter_category_id=filter_category_id, filter_ean=filter_ean,
                                         filter_sku=filter_sku, filter_name=filter_name,
                                         filter_price_from=filter_price_from,
                                         filter_price_to=filter_price_to, filter_stock_from=filter_stock_from,
                                         page=page, filter_sort=filter_sort)


    def get_inventory_products_stock(self, inventory_id, page=None):
        """
            The method allows you to retrieve detailed data for selected products from the BaseLinker catalogue.
        Keywords:
            inventory_id int: (required) Catalog ID. The list of identifiers can be retrieved
            by the get_inventories method
            page int (optional) Results paging (1000 products per page for BaseLinker warehouse)
        """
        return self.request.make_request('getInventoryProductsStock', inventory_id=inventory_id, page=page)


    def update_inventory_products_stock(self, inventory_id, products):
        """
            The method allows to update stocks of products (and/or their variants) in BaseLinker catalog. Maximum 1000 products at a time.
        Keywords:
            inventory_id int: (required) Catalog ID. The list of identifiers can be retrieved
            by the get_inventories method
            products array (required) An array of products, where the key is a product ID and the value is a list of stocks.
            When determining the variant stock, provide variant ID as a product ID.
            In the stocks array the key should be the warehouse ID and the value - stock for that warehouse.
            The format of the warehouse identifier should be as follows:
            "[type:bl|shop|warehouse]_[id:int]". (e.g. "bl_123").
            The list of warehouse identifiers can be retrieved using the get_inventory_warehouses method.
            Stocks cannot be assigned to the warehouses created automatically for
            purposes of keeping external stocks (shops, wholesalers, etc.).
        """
        return self.request.make_request('updateInventoryProductsStock', inventory_id=inventory_id, products=products)


    def get_inventory_products_prices(self, inventory_id, page=None):
        """
            The method allows to retrieve the gross prices of products from BaseLinker catalogues.
        Keywords:
            inventory_id int: (required) Catalog ID. The list of identifiers can be retrieved
            by the get_inventories method
            page int (optional) Results paging (1000 products per page for BaseLinker warehouse)
        """
        return self.request.make_request('getInventoryProductsPrices', inventory_id=inventory_id, page=page)


    def update_inventory_products_prices(self, inventory_id, products):
        """
            The method allows to retrieve the gross prices of products from BaseLinker catalogues.
        Keywords:
            inventory_id int: (required) Catalog ID. The list of identifiers can be retrieved
            by the get_inventories method
            products array (required) Lista z produktami, w której kluczem jest identyfikator produktu, a wartością lista cen.
            W przypadku określania cen dla wariantu należy podać identyfikator wariantu jako identyfikator produktu.
            W Liście cen kluczem powinien być identyfikator grupy cenowej, a wartością stan magazynowy dla tego magazynu.
             Listę grup cenowych mozna pobrać za pomocą metody get_inventory_price_groups.
        """
        return self.request.make_request('updateInventoryProductsPrices', inventory_id=inventory_id, products=products)


    def get_inventory_product_logs(self, product_id, date_from=None, date_to=None, log_type=None, sort=None, page=None):
        """
            The method allows to retrieve a list of events related to product change (or their variants) in the BaseLinker catalog.
        Keywords:
            product_id int: (required) Product identifier. In case of retrieving logs for a variant,
            the variant identifier must be provided as the product identifier.
            date_from int (optional) Date from which logs are to be retrieved. Unix time stamp format.
            date_to	int	(optional) Date up to which logs are to be retrieved. Unix time stamp format.
            log_type int (optional) List of event types you want to retrieve. Available values:
                1 - Change in stock
                2 - Price change
                3 - Product creation
                4 - Product deletion
                5 - Text fields modifications
                6 - Locations modifications
                7 - Modifications of links
                8 - Gallery modifications
                9 - Variant modifications
                10 - Modifications of bundle products
            sort int(optional) Type of log sorting. Possible "ASC" values ( ascending from date), "DESC" (descending after the date).
            By default the sorting is done in ascending order.
            page int (optional) Results paging (100 product editions per page).
        """
        return self.request.make_request('getInventoryProductLogs', product_id=product_id, date_from=date_from,
                                         date_to=date_to, log_type=log_type, sort=sort, page=page)