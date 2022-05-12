from .request import Request
from .orders import Orders
from .external_storages import ExternalStorages
from .product_catalog import ProductCatalog


class Baselinker:
    """Baselinker API client"""

    def __init__(self, api_token):
        self.api_token = api_token
        self.request = Request(self.api_token)
        self.orders = Orders(self.api_token)
        self.external_storages = ExternalStorages(self.api_token)
        self.product_catalog = ProductCatalog(self.api_token)