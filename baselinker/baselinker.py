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

    def get_orders(self, **kwargs):
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
        return self._make_request('getOrders', **kwargs)

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

