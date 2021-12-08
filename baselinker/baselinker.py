import json
import requests


class Baselinker:
    """Baselinker API client"""

    def __init__(self, api_token):
        self.api_token = api_token
        assert api_token != '', 'Must supply a non-empty API key.'
        self.api_url = 'https://api.baselinker.com/connector.php'

    def _get_request_data(self, method_name, parameters=None):
        request_data = {}
        request_data['method'] = method_name
        if parameters:
            request_data['parameters'] = json.dumps(parameters)
        return request_data

    def _get_request_headers(self):
        headers = {}
        headers['X-BLToken'] = self.api_token
        return headers

    def _make_request(self, method_name, **kwargs):
        requests_data = self._get_request_data(method_name, kwargs)
        headers = self._get_request_headers()
        try:
            with requests.Session() as s:
                response = s.post(self.api_url, data=requests_data, headers=headers)
                content = json.loads(response.content.decode("utf-8"))
                return content

        except requests.RequestException as e:
            print(e)
            raise e

    def get_orders(self, order_id=None, date_confirmed_from=None, date_from=None, id_from=None,
                   get_unconfirmed_orders=None, status_id=None, filter_email=None):
        """
        Method allows you to download orders from a specific date from the BaseLinker order manager.
        Keywords:
            order_id (int): (optional) Order identifier. Completing this field will download information about only one specific order.
            date_confirmed_from (int): (optional) Date of order confirmation from which orders are to be collected. Format unix time stamp.
            date_from (int): (optional) (optional) The order date from which orders are to be collected. Format unix time stamp.
            id_from	 (int): (optional) The order ID number from which subsequent orders are to be collected.
            get_unconfirmed_orders (bool): (optional, false by default) Download unconfirmed orders as well (this is e.g. an order from Allegro to which the customer has not yet completed the delivery form).
                                                                       Default is false. Unconfirmed orders may not be complete yet, the shipping method and price is also unknown.
            status_id (int): (optional) The status identifier from which orders are to be collected. Leave blank to download orders from all statuses.
            filter_email varchar(50): (optional) Filtering of order lists by e-mail address (displays only orders with the given e-mail address).
        """
        return self._make_request('getOrders', order_id=order_id, date_confirmed_from=date_confirmed_from,
                                  date_from=date_from, id_from=id_from,
                                  get_unconfirmed_orders=get_unconfirmed_orders,
                                  status_id=status_id, filter_email=filter_email)

    def get_order_sources(self):
        """
        The method returns types of order sources along with their IDs. Order sources are grouped by their type that
        corresponds to a field order_source from the getOrders method. Available source types are "personal", "shop"
        or "marketplace_code" e.g. "ebay", "amazon", "ceneo", "emag", "allegro", etc.
        """
        return self._make_request('getOrderSources')

    def get_order_transaction_details(self, order_id):
        """
              The method allows you to retrieve transaction details for a selected order (it now works only for orders from Amazon)
        Keywords:
            order_id (int): (optional) Order Identifier from BaseLinker order manager.
        """
        return self._make_request('getOrderTransactionDetails', order_id=order_id)

    def get_orders_by_email(self, email):
        """
              The method allows to search for orders related to the given e-mail address.
        Keywords:
            email (varchar(50): (required) The e-mail address we search for in orders.
        """
        return self._make_request('getOrdersByEmail', email=email)

    def get_orders_by_phone(self, phone):
        """
              The method allows you to search for orders related to the given phone number.
        Keywords:
            phone (varchar(50): (required) The phone number we search for in orders.
        """
        return self._make_request('getOrdersByPhone', phone=phone)

    def add_invoice(self, order_id, series_id):
        """
              The method allows to issue an order invoice.
        Keywords:
            order_id (int): (required) Order Identifier from BaseLinker order manager.
            series_id (int): (required) Series numbering identifier
        """
        return self._make_request('addInvoice', order_id=order_id, series_id=series_id)

    def get_invoices(self, invoice_id=None, order_id=None, date_from=None,
                     id_from=None, series_id=None, get_external_invoices=None):
        """
              The method allows you to download invoices issued from the BaseLinker order manager.
              The list of invoices can be limited using filters described in the method parameters.
               Maximum 100 invoices are returned at a time.
        Keywords:
            invoice_id (int): (optional) Invoice identifier. Completing this field will result in downloading
            information about only one specific invoice.
            order_id (int): (optional) Order identifier. Completing this field will result in downloading information
            only about the invoice associated with this order (if the order has an invoice created).
            date_from (int): (optional) Date from which invoices are to be collected. Unix time stamp format.
            id_from	(int): (optional) The invoice ID number from which subsequent invoices are to be retrieved.
            series_id (int): (optional) numbering series ID that allows filtering after the invoice numbering series.
            get_external_invoices (bool): (optional, true by default) Download external invoices as well.
        """
        return self._make_request('getInvoices', invoice_id=invoice_id, order_id=order_id, date_from=date_from,
                                  id_from=id_from, series_id=series_id, get_external_invoices=get_external_invoices)

    def get_series(self):
        """
              The method allows to download a series of invoice/receipt numbering.
        """
        return self._make_request('getSeries')

    def get_order_status_list(self):
        """
              The method allows you to download order statuses created by the customer in the BaseLinker order manager.
        """
        return self._make_request('getOrderStatusList')

    def get_order_payments_history(self, order_id=None, show_full_history=None):
        """
              The method allows you to retrieve payment history for a selected order,
              including an external payment identifier from the payment gateway.
              One order can have multiple payment history entries,caused by surcharges,
              order value changes, manual payment editing
        Keywords:
            order_id (int): (required) Order Identifier from BaseLinker order manager.
            show_full_history (bool): (optional, false by default) Download full payment history,
            including order value change entries, manual order payment edits.
            False by default - only returns entries containing an external payment identifier (most commonly used)
        """
        return self._make_request('getOrderPaymentsHistory', order_id=order_id, show_full_history=show_full_history)

    def get_new_receipts(self, series_id=None):
        """
             The method allows you to retrieve receipts waiting to be issued.
             This method should be used in creating integration with a fiscal printer.
             The method can be requested for new receipts every e.g. 10 seconds.
             If any receipts appear in response, they should be confirmed by the setOrderReceipt method
             after printing to disappear from the waiting list.
        Keywords:
            series_id (int): (optional) The numbering series ID allows filtering by the receipt numbering series.
            Using multiple series numbering for receipts is recommended when the user has multiple fiscal printers.
            Each fiscal printer should have a separate series.
        """
        return self._make_request('getNewReceipts', series_id=series_id)

    def get_receipt(self, receipt_id=None, order_id=None):
        """
            The method allows you to retrieve a single receipt from the BaseLinker order manager.
            To retrieve a list of new receipts (when integrating a fiscal printer), use the getNewReceipts method.
        Keywords:
            receipt_id (int): Receipt ID. Not required if order_id is provided.
            order_id (int): Order ID. Not required if receipt_id is provided.
        """
        return self._make_request('getReceipt', receipt_id=receipt_id, order_id=order_id)

    def set_order_fields(self, order_id=None, admin_comments=None, user_comments=None, payment_method=None,
                         payment_method_cod=None, email=None, phone=None, user_login=None, delivery_method=None,
                         delivery_price=None, delivery_fullname=None, delivery_company=None, delivery_address=None,
                         delivery_postcode=None, delivery_city=None, delivery_country_code=None,
                         delivery_point_id=None,
                         delivery_point_name=None, delivery_point_address=None, delivery_point_postcode=None,
                         delivery_point_city=None, invoice_fullname=None, invoice_company=None, invoice_nip=None,
                         invoice_address=None, invoice_postcode=None, invoice_city=None, invoice_country_code=None,
                         want_invoice=None, extra_field_1=None, extra_field_2=None, pick_state=None,
                         pack_state=None):
        """
            The method allows you to edit selected fields (e.g. address data, notes, etc.) of a specific order.
            Only the fields that you want to edit should be given, other fields can be omitted in the request.
        Keywords:
            admin_comments varchar(200) Seller comments
            user_comments varchar(510) Buyer comments
            payment_method varchar(30) Payment method
            payment_method_cod (bool) Flag indicating whether the type of payment is COD (cash on delivery)
            email varchar(150) Buyer e-mail address
            phone varchar(100) Buyer phone number
            user_login	varchar(30)	Buyer login
            delivery_method	varchar(30)	Delivery method name
            delivery_price	(float)	Gross delivery price
            delivery_fullname varchar(100) Delivery address - name and surname
            delivery_company varchar(100) Delivery address - company
            delivery_address varchar(100) Delivery address - street and number
            delivery_postcode varchar(100) Delivery address - postcode
            delivery_city varchar(100) Delivery address - city
            delivery_country_code char(2) Delivery address - country code (two-letter, e.g. EN)
            delivery_point_id varchar(40) Pick-up point delivery - pick-up point identifier
            delivery_point_name varchar(100) Pick-up point delivery - pick-up point name
            delivery_point_address varchar(100)	Pick-up point delivery - pick-up point address
            delivery_point_postcode varchar(100) Pick-up point delivery - pick-up point postcode
            delivery_point_city varchar(100) Pick-up point delivery - pick-up point city
            invoice_fullname varchar(100) Billing details - name and surname
            invoice_company varchar(100) Billing details - company
            invoice_nip varchar(100) Billing details - Vat Reg. no./tax number
            invoice_address varchar(100) Billing details - street and house number
            invoice_postcode varchar(100) Billing details - postcode
            invoice_city varchar(100) Billing details - city
            invoice_country_code char(2) Billing details - country code (two-letter, e.g. EN)
            want_invoice (bool)	Flag indicating whether the customer wants an invoice (1 - yes, 0 - no)
            extra_field_1 varchar(50) Value from "extra field 1". - the seller can store any information there
            extra_field_2 varchar(50) Value from "extra field 2". - the seller can store any information there
            pick_state (int) Flag indicating the status of the order products collection (1 - all products have been collected, 0 - not all products have been collected)
            pack_state (int) Flag indicating the status of the order products packing (1 - all products have been packed, 0 - not all products have been packed)
        """
        return self._make_request('setOrderFields', order_id=order_id, admin_comments=admin_comments,
                                  user_comments=user_comments,
                                  payment_method=payment_method, payment_method_cod=payment_method_cod, email=email,
                                  phone=phone, user_login=user_login,
                                  delivery_method=delivery_method, delivery_price=delivery_price,
                                  delivery_fullname=delivery_fullname, delivery_company=delivery_company,
                                  delivery_address=delivery_address, delivery_postcode=delivery_postcode,
                                  delivery_city=delivery_city, delivery_country_code=delivery_country_code,
                                  delivery_point_id=delivery_point_id, delivery_point_name=delivery_point_name,
                                  delivery_point_address=delivery_point_address,
                                  delivery_point_postcode=delivery_point_postcode,
                                  delivery_point_city=delivery_point_city,
                                  invoice_fullname=invoice_fullname, invoice_company=invoice_company,
                                  invoice_nip=invoice_nip, invoice_address=invoice_address,
                                  invoice_postcode=invoice_postcode, invoice_city=invoice_city,
                                  invoice_country_code=invoice_country_code,
                                  want_invoice=want_invoice, extra_field_1=extra_field_1,
                                  extra_field_2=extra_field_2,
                                  pick_state=pick_state, pack_state=pack_state)

    def add_order_product(self, order_id=None, storage=None, storage_id=None,
                          product_id=None, variant_id=None, auction_id=None,
                          name=None, sku=None, ean=None, attributes=None,
                          price_brutto=None, tax_rate=None, quantity=None, weight=None):
        """
             The method allows you to add a new product to your order.
        Keywords:
            order_id (int) Order Identifier from BaseLinker order manager
            storage	varchar(9) Type of product source storage (available values: "db" - BaseLinker internal catalog, "shop" - online shop storage, "warehouse" - the connected wholesaler)
            storage_id varchar(50) ID of the product source storage (one from BaseLinker catalogs or one of the stores connected to the account). Value "0" when the product comes from BaseLinker internal catalog.
            product_id varchar(50) Product identifier in BaseLinker or shop storage. Blank if the product number is not known
            variant_id varchar(30) Product variant ID. Blank if the variant number is unknown
            auction_id varchar(20) Listing ID number (if the order comes from ebay/allegro)
            name varchar(130) Product name
            sku	varchar(40)	Product SKU number
            ean	varchar(40)	Product EAN number
            attributes varchar(150) The detailed product attributes, e.g. "Colour: blue" (Variant name)
            price_brutto (float) Single item gross price
            tax_rate (float) VAT rate
            quantity (int) Number of pieces
            weight (float) Single piece weight
        """
        return self._make_request('addOrderProduct', order_id=order_id, storage=storage, storage_id=storage_id,
                                  product_id=product_id, variant_id=variant_id, auction_id=auction_id,
                                  name=name, sku=sku, ean=ean, attributes=attributes,
                                  price_brutto=price_brutto, tax_rate=tax_rate, quantity=quantity, weight=weight)

    def set_order_product_fields(self, order_id, order_product_id, storage=None, storage_id=None,
                                 product_id=None, variant_id=None, auction_id=None,
                                 name=None, sku=None, ean=None, attributes=None,
                                 price_brutto=None, tax_rate=None, quantity=None, weight=None):
        """
             The method allows you to edit the data of selected items (e.g. prices, quantities etc.) of a specific order.
              Only the fields that you want to edit should be given, the remaining fields can be omitted in the request.
        Keywords:
            order_id (int): (required) Order Identifier from BaseLinker order manager
            order_product_id (int): (required) Order item ID from BaseLinker order manager. Field required.
            storage	varchar(9) Type of product source storage (available values: "db" - BaseLinker internal catalog, "shop" - online shop storage, "warehouse" - the connected wholesaler)
            storage_id varchar(50) ID of the product source storage (one from BaseLinker catalogs or one of the stores connected to the account). Value "0" when the product comes from BaseLinker internal catalog.
            product_id varchar(50) Product identifier in BaseLinker or shop storage. Blank if the product number is not known
            variant_id varchar(30) Product variant ID. Blank if the variant number is unknown
            auction_id varchar(20) Listing ID number (if the order comes from ebay/allegro)
            name varchar(130) Product name
            sku	varchar(40)	Product SKU number
            ean	varchar(40)	Product EAN number
            attributes varchar(150) The detailed product attributes, e.g. "Colour: blue" (Variant name)
            price_brutto (float) Single item gross price
            tax_rate (float) VAT rate
            quantity (int) Number of pieces
            weight (float) Single piece weight
        """
        return self._make_request('setOrderProductFields', order_id=order_id, order_product_id=order_product_id,
                                  storage=storage, storage_id=storage_id, product_id=product_id,
                                  variant_id=variant_id,
                                  auction_id=auction_id, name=name, sku=sku, ean=ean, attributes=attributes,
                                  price_brutto=price_brutto, tax_rate=tax_rate, quantity=quantity, weight=weight)

    def delete_order_product(self, order_id, order_product_id):
        """
              The method allows you to remove a specific product from the order.
        Keywords:
            order_id (int): (required) Order Identifier from BaseLinker order manager.
            order_product_id (int): (required) Order item ID from BaseLinker order manager.
        """
        return self._make_request('deleteOrderProduct', order_id=order_id, order_product_id=order_product_id)

    def set_order_payment(self, order_id, payment_done, payment_date, payment_comment):
        """
              The method allows you to add a payment to the order.
        Keywords:
            order_id (int): (required) Order ID number
            payment_done (float): (required) The amount of the payment. The value changes the current payment in the order
                                (not added to the previous value).
                                If the amount matches the order value, the order will be marked as paid.
            payment_date (int): (required) Payment date unixtime.
            payment_comment varchar(30): (required) Payments commentary.
        """
        return self._make_request('setOrderPayment', order_id=order_id, payment_done=payment_done,
                                  payment_date=payment_date, payment_comment=payment_comment)

    def set_order_status(self, order_id, status_id):
        """
              The method allows you to change order status.
        Keywords:
            order_id (int): (required) Order ID number
            status_id (int): (required) Status ID number. The status list can be retrieved using getOrderStatusList.
        """
        return self._make_request('setOrderStatus', order_id=order_id, status_id=status_id)

    def set_order_receipt(self, receipt_id, receipt_nr, date, printer_error=None):
        """
              The method allows you to mark orders with a receipt already issued.
        Keywords:
            receipt_id (int): (required) Receipt_id number received in the get_new_receipts method
            receipt_nr varchar(20): (required) The number of the issued receipt (may be blank if the printer does not return the number)
            date (int): (required) Receipt printing date (unixtime format)
            printer_error (bool): Flag indicating whether an error occurred during receipt printing (false by default)
        """
        return self._make_request('setOrderReceipt', receipt_id=receipt_id, receipt_nr=receipt_nr,
                                  date=date, printer_error=printer_error)

    def add_order_invoice_file(self, invoice_id, file, external_invoice_number):
        """
              The method allows you to mark orders with a receipt already issued.
        Keywords:
            invoice_id (int): (required) BaseLinker invoice identifier
            file (text): (required) Invoice PDF file in binary format encoded in base64,
            at the very beginning of the invoice string provide a prefix "data:" e.g. "data:4AAQSkSzkJRgABA[...]"
            external_invoice_number varchar(30): (required) External system invoice number (overwrites BaseLinker invoice number)
        """
        return self._make_request('addOrderInvoiceFile', invoice_id=invoice_id, file=file,
                                  external_invoice_number=external_invoice_number)

    def get_external_storages_list(self):
        """
              The method allows you to retrieve a list of available external storages (shops, wholesalers)
              that can be referenced via API.
        """
        return self._make_request('getExternalStoragesList')

    def get_external_storage_categories(self, storage_id):
        """
              The method allows you to retrieve a category list from an external storage (shop/wholesale)
              connected to BaseLinker.
        Keywords:
            storage_id varchar(30): (required) Storage ID in format "[type:shop|warehouse]_[id:int]" (e.g. "shop_2445").
        """
        return self._make_request('getExternalStorageCategories', storage_id=storage_id)

    def get_external_storage_products_data(self, storage_id, products):
        """
              The method allows you to retrieve a category list from an external storage (shop/wholesale)
              connected to BaseLinker.
        Keywords:
            storage_id varchar(30): (required) Storage ID in format "[type:shop|warehouse]_[id:int]" (e.g. "shop_2445").
            products array: (required) An array of product ID numbers to download
        """
        return self._make_request('getExternalStorageProductsData', storage_id=storage_id, products=products)

    def get_external_storage_products_list(self, storage_id, filter_category_id=None, filter_sort=None, filter_id=None,
                                           filter_ean=None, filter_sku=None, filter_name=None, filter_price_from=None,
                                           filter_price_to=None,  filter_quantity_from=None, filter_quantity_to=None,
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
        return self._make_request('getExternalStorageProductsList', storage_id=storage_id, filter_category_id=filter_category_id,
                                  filter_sort=filter_sort, filter_id=filter_id, filter_ean=filter_ean,
                                  filter_sku=filter_sku, filter_name=filter_name, filter_price_from=filter_price_from,
                                  filter_price_to=filter_price_to, filter_quantity_from=filter_quantity_from,
                                  filter_quantity_to=filter_quantity_to, filter_available=filter_available, page=page)

    def get_external_storage_products_quantity(self, storage_id, page):
        """
              The method allows you to retrieve a category list from an external storage (shop/wholesale)
              connected to BaseLinker.
        Keywords:
            storage_id varchar(30): (required) Storage ID in format "[type:shop|warehouse]_[id:int]" (e.g. "shop_2445").
            page (int): (optional) pagination
        """
        return self._make_request('getExternalStorageProductsQuantity', storage_id=storage_id, page=page)

    def get_external_storage_products_prices(self, storage_id, page):
        """
              The method allows you to retrieve a category list from an external storage (shop/wholesale)
              connected to BaseLinker.
        Keywords:
            storage_id varchar(30): (required) Storage ID in format "[type:shop|warehouse]_[id:int]" (e.g. "shop_2445").
            page (int): (optional) pagination
        """
        return self._make_request('getExternalStorageProductsPrices', storage_id=storage_id, page=page)

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
        return self._make_request('updateExternalStorageProductsQuantity', storage_id=storage_id, products=products)

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
        return self._make_request('addInventoryPriceGroup', price_group_id=price_group_id, name=name,
                                  description=description, currency=currency)

    def delete_inventory_price_group(self, price_group_id):
        """
            The method allows you to remove the price group from BaseLinker storage.
        Keywords:
            price_group_id int: (required) Price group identifier
        """
        return self._make_request('deleteInventoryPriceGroup', price_group_id=price_group_id)

    def get_inventory_price_groups(self):
        """
            The method allows to retrieve price groups existing in BaseLinker storage
        """
        return self._make_request('getInventoryPriceGroups')

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
        return self._make_request('addInventoryWarehouse', warehouse_id=warehouse_id, name=name,
                                  description=description, stock_edition=stock_edition)

    def delete_inventory_warehouse(self, warehouse_id):
        """
           The method allows you to remove the warehouse available in BaseLinker catalogues.
           The method does not allow to remove warehouses created automatically
           for the purpose of keeping external stocks of shops, wholesalers etc.
        Keywords:
            warehouse_id int: (required) ID of the warehouse
        """
        return self._make_request('deleteInventoryWarehouse', warehouse_id=warehouse_id)

    def get_inventory_warehouses(self):
        """
        The method allows you to retrieve a list of warehouses available in BaseLinker catalogues.
        The method also returns information about the warehouses created automatically
        for the purpose of keeping external stocks (shops, wholesalers etc.)
        """
        return self._make_request('getInventoryWarehouses')

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
        return self._make_request('addInventory', inventory_id=inventory_id, name=name,
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
        return self._make_request('deleteInventory', inventory_id=inventory_id)

    def get_inventories(self):
        """
         The method allows you to retrieve a list of catalogs available in the BaseLinker storage.
        """
        return self._make_request('getInventories')

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
        return self._make_request('addInventoryCategory', inventory_id=inventory_id, category_id=category_id,
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
        return self._make_request('deleteInventoryCategory', category_id=category_id)

    def get_inventory_categories(self, inventory_id):
        """
         The method allows you to retrieve a list of categories for a BaseLinker catalog.
        Keywords:
            inventory_id int: (required) Catalog ID. The list of identifiers can be retrieved by
            the get_inventories method (inventory_id field).
            To retrieve categories available for all catalogs created in BaseLinker, this field should be omitted.
        """
        return self._make_request('getInventoryCategories', inventory_id=inventory_id)

    def add_inventory_manufacturer(self, manufacturer_id, name):
        """
         The method allows you to retrieve a list of categories for a BaseLinker catalog.
        Keywords:
            manufacturer_id int: (required) Manufacturer ID provided in case of an update. Should be blank when creating a new manufacturer.
            name varchar(200): (required) Manufacturer name
        """
        return self._make_request('addInventoryManufacturer', manufacturer_id=manufacturer_id, name=name)

    def delete_inventory_manufacturer(self, manufacturer_id):
        """
         The method allows you to remove manufacturer from BaseLinker catalog
        Keywords:
            manufacturer_id int: (required) The ID of the manufacturer removed from BaseLinker warehouse.
        """
        return self._make_request('deleteInventoryManufacturer', manufacturer_id=manufacturer_id)

    def get_inventory_manufacturers(self):
        """
         The method allows you to retrieve a list of manufacturers for a BaseLinker catalog.
        """
        return self._make_request('getInventoryManufacturers')

    def get_inventory_extra_fields(self):
        """
         The method allows you to retrieve a list of extra fields for a BaseLinker catalog.
        """
        return self._make_request('getInventoryExtraFields')

    def get_inventory_integrations(self, inventory_id):
        """
         The method returns a list of integrations where text values in the catalog can be overwritten.
         The returned data contains a list of accounts for each integration
         and a list of languages supported by the integration
        Keywords:
            inventory_id int: (required) Catalog ID.
            The list of identifiers can be retrieved using the method get_inventories. (inventory_id field).
        """
        return self._make_request('getInventoryIntegrations', inventory_id=inventory_id)

    def get_inventory_available_text_field_keys(self, inventory_id):
        """
         The method returns a list of product text fields that can be overwritten for specific integration.
        Keywords:
            inventory_id int: (required) Catalog ID. The list of identifiers can be retrieved
            by the get_inventories method (inventory_id field).
        """
        return self._make_request('getInventoryAvailableTextFieldKeys', inventory_id=inventory_id)

    def delete_inventory_product(self, product_id):
        """
         The method allows you to remove the product from BaseLinker catalog.
        Keywords:
            product_id int: (required) BaseLinker catalogue product identifier
        """
        return self._make_request('deleteInventoryProduct', product_id=product_id)

    def get_inventory_products_data(self, inventory_id, products):
        """
         The method allows you to retrieve detailed data for selected products from the BaseLinker catalogue.
        Keywords:
            inventory_id int: (required) Catalog ID. The list of identifiers can be retrieved
            by the get_inventories method (inventory_id field).
            products array (required) An array of product ID numbers to download
        """
        return self._make_request('getInventoryProductsData', inventory_id=inventory_id, products=products)

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
        return self._make_request('getInventoryProductsList', inventory_id=inventory_id, filter_id=filter_id,
                                  filter_category_id=filter_category_id, filter_ean=filter_ean,
                                  filter_sku=filter_sku, filter_name=filter_name, filter_price_from=filter_price_from,
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
        return self._make_request('getInventoryProductsStock', inventory_id=inventory_id, page=page)

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
        return self._make_request('updateInventoryProductsStock', inventory_id=inventory_id, products=products)

    def get_inventory_products_prices(self, inventory_id, page=None):
        """
         The method allows to retrieve the gross prices of products from BaseLinker catalogues.
        Keywords:
            inventory_id int: (required) Catalog ID. The list of identifiers can be retrieved
            by the get_inventories method
            page int (optional) Results paging (1000 products per page for BaseLinker warehouse)
        """
        return self._make_request('getInventoryProductsPrices', inventory_id=inventory_id, page=page)

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
        return self._make_request('updateInventoryProductsPrices', inventory_id=inventory_id, products=products)

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
        return self._make_request('getInventoryProductLogs', product_id=product_id, date_from=date_from,
                                  date_to=date_to, log_type=log_type, sort=sort, page=page)