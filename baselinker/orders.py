from .request import Request


class Orders:
    def __init__(self, api_token):
        self.api_token = api_token
        self.request = Request(self.api_token)

    def get_journal_list(self, last_log_id, logs_types, order_id):
        """
            The method allows you to download a list of order events from the last 3 days.
        Keywords:
            last_log_id	(int): (required) Log ID number from which the logs are to be retrieved
            logs_types (array): (required) Event ID List
            order_id (int): (required) Order ID number
        """
        return self.request.make_request('getJournalList', last_log_id=last_log_id, logs_types=logs_types,
                                         order_id=order_id)

    def get_order_extra_fields(self):
        """
            The method returns extra fields defined for the orders.
            Values of those fields can be set with method set_order_fields.
            In order to retrieve values of those fields set parameter include_custom_extra_fields in method get_orders
        """
        return self.request.make_request('getOrderExtraFields')

    def get_orders(self, order_id=None, date_confirmed_from=None, date_from=None, id_from=None,
                   get_unconfirmed_orders=None, status_id=None, filter_email=None):
        """
            Method allows you to download orders from a specific date from the BaseLinker order manager.
        Keywords:
            order_id (int): (optional) Order identifier. Completing this field will download
            information about only one specific order.
            date_confirmed_from (int): (optional) Date of order confirmation from which orders are to be collected.
            Format unix time stamp.
            date_from (int): (optional) (optional) The order date from which orders are to be collected.
            Format unix time stamp.
            id_from	 (int): (optional) The order ID number from which subsequent orders are to be collected.
            get_unconfirmed_orders (bool): (optional, false by default) Download unconfirmed orders as well
            (this is e.g. an order from Allegro to which the customer has not yet completed the delivery form).
            Default is false. Unconfirmed orders may not be complete yet, the shipping method and price is also unknown.
            status_id (int): (optional) The status identifier from which orders are to be collected.
            Leave blank to download orders from all statuses.
            filter_email varchar(50): (optional) Filtering of order lists by e-mail address
            (displays only orders with the given e-mail address).
        """
        return self.request.make_request('getOrders', order_id=order_id, date_confirmed_from=date_confirmed_from,
                                         date_from=date_from, id_from=id_from,
                                         get_unconfirmed_orders=get_unconfirmed_orders,
                                         status_id=status_id, filter_email=filter_email)

    def get_order_sources(self):
        """
            The method returns types of order sources along with their IDs. Order sources are grouped by their type that
            corresponds to a field order_source from the getOrders method. Available source types are "personal", "shop"
            or "marketplace_code" e.g. "ebay", "amazon", "ceneo", "emag", "allegro", etc.
        """
        return self.request.make_request('getOrderSources')

    def get_order_transaction_details(self, order_id):
        """
            The method allows you to retrieve transaction details for a selected order
            (it now works only for orders from Amazon)
        Keywords:
            order_id (int): (optional) Order Identifier from BaseLinker order manager.
        """
        return self.request.make_request('getOrderTransactionDetails', order_id=order_id)

    def get_orders_by_email(self, email):
        """
            The method allows to search for orders related to the given e-mail address.
        Keywords:
            email (varchar(50): (required) The e-mail address we search for in orders.
        """
        return self.request.make_request('getOrdersByEmail', email=email)

    def get_orders_by_phone(self, phone):
        """
            The method allows you to search for orders related to the given phone number.
        Keywords:
            phone (varchar(50): (required) The phone number we search for in orders.
        """
        return self.request.make_request('getOrdersByPhone', phone=phone)

    def add_invoice(self, order_id, series_id):
        """
            The method allows to issue an order invoice.
        Keywords:
            order_id (int): (required) Order Identifier from BaseLinker order manager.
            series_id (int): (required) Series numbering identifier
        """
        return self.request.make_request('addInvoice', order_id=order_id, series_id=series_id)

    def get_invoices(self, invoice_id=None, order_id=None, date_from=None,
                     id_from=None, series_id=None, get_external_invoices=None):
        """
            The method allows you to download invoices issued from the BaseLinker order manager.
            the list of invoices can be limited using filters described in the method parameters.
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
        return self.request.make_request('getInvoices', invoice_id=invoice_id, order_id=order_id,
                                         date_from=date_from, id_from=id_from, series_id=series_id,
                                         get_external_invoices=get_external_invoices)

    def get_series(self):
        """
            The method allows to download a series of invoice/receipt numbering.
        """
        return self.request.make_request('getSeries')

    def get_order_status_list(self):
        """
            The method allows you to download order statuses created by the customer in the BaseLinker order manager.
        """
        return self.request.make_request('getOrderStatusList')

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
        return self.request.make_request('getOrderPaymentsHistory', order_id=order_id,
                                         show_full_history=show_full_history)

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
        return self.request.make_request('getNewReceipts', series_id=series_id)

    def get_receipt(self, receipt_id=None, order_id=None):
        """
            The method allows you to retrieve a single receipt from the BaseLinker order manager.
            To retrieve a list of new receipts (when integrating a fiscal printer), use the getNewReceipts method.
        Keywords:
            receipt_id (int): Receipt ID. Not required if order_id is provided.
            order_id (int): Order ID. Not required if receipt_id is provided.
        """
        return self.request.make_request('getReceipt', receipt_id=receipt_id, order_id=order_id)

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
            pick_state (int) Flag indicating the status of the order products collection
            (1 - all products have been collected, 0 - not all products have been collected)
            pack_state (int) Flag indicating the status of the order products packing
            (1 - all products have been packed, 0 - not all products have been packed)
        """
        return self.request.make_request('setOrderFields', order_id=order_id, admin_comments=admin_comments,
                                         user_comments=user_comments,
                                         payment_method=payment_method, payment_method_cod=payment_method_cod,
                                         email=email,
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
            storage	varchar(9) Type of product source storage (available values: "db" - BaseLinker internal catalog,
            "shop" - online shop storage, "warehouse" - the connected wholesaler)
            storage_id varchar(50) ID of the product source storage
            (one from BaseLinker catalogs or one of the stores connected to the account).
            Value "0" when the product comes from BaseLinker internal catalog.
            product_id varchar(50) Product identifier in BaseLinker or shop storage.
            Blank if the product number is not known
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
        return self.request.make_request('addOrderProduct', order_id=order_id, storage=storage, storage_id=storage_id,
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
            storage	varchar(9) Type of product source storage
            (available values: "db" - BaseLinker internal catalog, "shop" - online shop storage,
            "warehouse" - the connected wholesaler)
            storage_id varchar(50) ID of the product source storage
            (one from BaseLinker catalogs or one of the stores connected to the account).
            Value "0" when the product comes from BaseLinker internal catalog.
            product_id varchar(50) Product identifier in BaseLinker or shop storage. Blank if the product number is not
            known variant_id varchar(30) Product variant ID. Blank if the variant number is unknown
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
        return self.request.make_request('setOrderProductFields', order_id=order_id, order_product_id=order_product_id,
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
        return self.request.make_request('deleteOrderProduct', order_id=order_id, order_product_id=order_product_id)

    def set_order_payment(self, order_id, payment_done, payment_date, payment_comment):
        """
            The method allows you to add a payment to the order.
        Keywords:
            order_id (int): (required) Order ID number
            payment_done (float): (required) The amount of the payment. The value changes the current payment in the
            order (not added to the previous value). If the amount matches the order value,
            the order will be marked as paid.
            payment_date (int): (required) Payment date unixtime.
            payment_comment varchar(30): (required) Payments commentary.
        """
        return self.request.make_request('setOrderPayment', order_id=order_id, payment_done=payment_done,
                                         payment_date=payment_date, payment_comment=payment_comment)

    def set_order_status(self, order_id, status_id):
        """
            The method allows you to change order status.
        Keywords:
            order_id (int): (required) Order ID number
            status_id (int): (required) Status ID number. The status list can be retrieved using getOrderStatusList.
        """
        return self.request.make_request('setOrderStatus', order_id=order_id, status_id=status_id)

    def set_order_receipt(self, receipt_id, receipt_nr, date, printer_error=None):
        """
            The method allows you to mark orders with a receipt already issued.
        Keywords:
            receipt_id (int): (required) Receipt_id number received in the get_new_receipts method
            receipt_nr varchar(20): (required) The number of the issued receipt
            (may be blank if the printer does not return the number)
            date (int): (required) Receipt printing date (unixtime format)
            printer_error (bool): Flag indicating whether an error occurred during receipt printing (false by default)
        """
        return self.request.make_request('setOrderReceipt', receipt_id=receipt_id, receipt_nr=receipt_nr,
                                         date=date, printer_error=printer_error)

    def add_order_invoice_file(self, invoice_id, file, external_invoice_number):
        """
            The method allows you to mark orders with a receipt already issued.
        Keywords:
            invoice_id (int): (required) BaseLinker invoice identifier
            file (text): (required) Invoice PDF file in binary format encoded in base64,
            at the very beginning of the invoice string provide a prefix "data:" e.g. "data:4AAQSkSzkJRgABA[...]"
            external_invoice_number varchar(30): (required) External system invoice number
            (overwrites BaseLinker invoice number)
        """
        return self.request.make_request('addOrderInvoiceFile', invoice_id=invoice_id, file=file,
                                         external_invoice_number=external_invoice_number)
