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
        request_data['token'] = self.api_token
        request_data['method'] = method_name
        if parameters:
            request_data['parameters'] = json.dumps(parameters)
        return request_data

    def _make_request(self, method_name, parameters=None):
        requests_data = self._get_request_data(method_name, parameters=None)

        try:
            with requests.Session() as s:
                response = s.post(self.api_url, data=requests_data)
                content = json.loads(response.content.decode("utf-8"))
                return content

        except requests.RequestException as e:
            print(e)
            raise e

    def get_orders(self, order_id=None, date_confirmed_from=None, date_from=None, id_from=None, get_unconfirmed_orders=False, status_id=None, filter_email=None):
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
        return self._make_request('getOrders')

    def get_order_sources(self):
        """
        The method returns types of order sources along with their IDs. Order sources are grouped by their type that
        corresponds to a field order_source from the getOrders method. Available source types are "personal", "shop"
        or "marketplace_code" e.g. "ebay", "amazon", "ceneo", "emag", "allegro", etc.
        """
        return self._make_request('getOrderSources')