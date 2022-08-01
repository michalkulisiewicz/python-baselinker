<img src="https://1.bp.blogspot.com/-a4AnsxS6-XQ/Xj6aIKumFpI/AAAAAAAAAEU/HCXJkmVPcy8FwpDag5-Fw_8KKFLTrxs-QCLcBGAsYHQ/s1600/baselinker.jpg" width="400"/>

A Python client library for accessing baselinker API.
List of the methods available [here](https://api.baselinker.com/)

## Installation
Use git clone to get the library
```
git clone git@github.com:michalkulisiewicz/python-baselinker.git
```
Install all requirements using pip
```python
pip install -r requirements.txt
```

## Quickstart
The token is assigned directly to the BaseLinker user account. User can generate API token in BaseLinker panel in "Account & other -> My account -> API" section.

```python
from baselinker import Baselinker

API_TOKEN = 'INSERT YOUR TOKEN HERE'


def run():
    # Create a baselinker client instance
    baselinker = Baselinker(API_TOKEN)
    # Prints 100 orders from baselinker
    print(baselinker.orders.get_orders())

    
if __name__ == '__main__':
    run()
```

# Usage
### Product catalog
```python
baselinker.orders.get_orders()
```
**Sample response:**
```python
{
    "status": "SUCCESS",
    "price_groups": [
        {
            "price_group_id": 104,
            "name": "Default",
            "description": "Default price group",
            "currency": "EUR",
            "is_default": true
        },
        {
            "price_group_id": 105,
            "name": "USA",
            "description": "Price group for US market",
            "currency": "USD",
            "is_default": false
        }
    ]
}
```

### External storages
```python
baselinker.external_storages.get_external_storages_list()
```
**Sample response:**
```python
{
    "status": "SUCCESS",
    "storages": [
        {
            "storage_id": "shop_2444",
            "name": "Online store",
            "methods": ["getExternalStorageCategories", "getExternalStorageProductsData", "getExternalStorageProductsList", "getExternalStorageProductsPrices", "getExternalStorageProductsQuantity", "updateExternalStorageProductsQuantity"]
        },
        {
            "storage_id": "warehouse_1334",
            "name": "Wholesaler",
            "methods": ["getExternalStorageCategories", "getExternalStorageProductsData", "getExternalStorageProductsList", "getExternalStorageProductsPrices", "getExternalStorageProductsQuantity"]
        },
    ]
}
```

### Orders
```python
baselinker.orders.get_orders()
```
**Sample response:**
```python
{
  "status": "SUCCESS",
  "orders": [
    {
      "order_id": "1630473",
      "shop_order_id": "2824",
      "external_order_id": "534534234",
      "order_source": "amazon",
      "order_source_id": "2598",
      "order_source_info": "-",
      "order_status_id": "6624",
      "date_add": "1407841161",
      "date_confirmed": "1407841256",
      "date_in_status": "1407841256",
      "user_login": "nick123",
      "phone": "693123123",
      "email": "test@test.com",
      "user_comments": "User comment",
      "admin_comments": "Seller test comments",
      "currency": "GBP",
      "payment_method": "PayPal",
      "payment_method_cod": "0",
      "payment_done": "50",
      "delivery_method": "Expedited shipping",
      "delivery_price": "10",
      "delivery_package_module": "other",
      "delivery_package_nr": "0042348723648234",
      "delivery_fullname": "John Doe",
      "delivery_company": "Company",
      "delivery_address": "Long Str 12",
      "delivery_city": "London",
      "delivery_postcode": "E2 8HQ",
      "delivery_country": "Great Britain",
      "delivery_point_id": "",
      "delivery_point_name": "",
      "delivery_point_address": "",
      "delivery_point_postcode": "",
      "delivery_point_city": "",
      "invoice_fullname": "John Doe",
      "invoice_company": "Company",
      "invoice_nip": "GB8943245",
      "invoice_address": "Long Str 12",
      "invoice_city": "London",
      "invoice_postcode": "E2 8HQ",
      "invoice_country": "Great Britain",
      "want_invoice": "0",
      "extra_field_1": "",
      "extra_field_2": "",
      "custom_extra_fields": {
          "135": "B2B",
          "172": "1646913115"
      },
      "order_page": "https://klient.baselinker.com/1630473/4ceca0d940/",
      "pick_status": "1",
      "pack_status": "0",
      "products": [
        {
          "storage": "shop"
          "storage_id": 1,
          "order_product_id": "154904741",
          "product_id": "5434",
          "variant_id": 52124,
          "name": "Harry Potter and the Chamber of Secrets",
          "attributes": "Colour: green",
          "sku": "LU4235",
          "ean": "1597368451236",
          "location": "A1-13-7",
          "auction_id": "0",
          "price_brutto": 20.00,
          "tax_rate": 23,
          "quantity": 2,
          "weight": 1,
          "bundle_id": 0
        }
      ]
    }
  ]
}
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/michalkulisiewicz/python-baselinker. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [code of conduct](https://github.com/michalkulisiewicz/python-baselinker/blob/master/CODE_OF_CONDUCT.md).

## License

Project is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

## Code of Conduct

Everyone that interacts in the project codebase, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/michalkulisiewicz/python-baselinker/blob/master/CODE_OF_CONDUCT.md)
