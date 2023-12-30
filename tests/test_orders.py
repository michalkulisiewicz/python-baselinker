import unittest
from unittest.mock import MagicMock
from baselinker.orders import Orders


class TestOrders(unittest.TestCase):
    def setUp(self):
        self.api_token = "my_token"
        self.orders = Orders(self.api_token)
        self.orders.request.make_request = MagicMock(return_value={"success": True})

    def test_get_journal_list(self):
        result = self.orders.get_journal_list(last_log_id=1, logs_types=["type1", "type2"], order_id=123)
        self.orders.request.make_request.assert_called_with('getJournalList', last_log_id=1,
                                                            logs_types=["type1", "type2"], order_id=123)
        self.assertTrue(result["success"])

    def test_get_order_extra_fields(self):
        result = self.orders.get_order_extra_fields()
        self.orders.request.make_request.assert_called_with('getOrderExtraFields')
        self.assertTrue(result["success"])

    def test_get_orders(self):
        result = self.orders.get_orders(order_id=123, date_confirmed_from=123456789, date_from=987654321, id_from=1,
                                        get_unconfirmed_orders=True, status_id=2, filter_email="test@example.com")
        self.orders.request.make_request.assert_called_with('getOrders', order_id=123, date_confirmed_from=123456789,
                                                            date_from=987654321, id_from=1, get_unconfirmed_orders=True,
                                                            status_id=2, filter_email="test@example.com")
        self.assertTrue(result["success"])

    def test_get_order_sources(self):
        result = self.orders.get_order_sources()
        self.orders.request.make_request.assert_called_with('getOrderSources')
        self.assertTrue(result["success"])

    def test_get_order_transaction_details(self):
        result = self.orders.get_order_transaction_details(order_id=123)
        self.orders.request.make_request.assert_called_with('getOrderTransactionDetails', order_id=123)
        self.assertTrue(result["success"])

    def test_get_orders_by_email(self):
        result = self.orders.get_orders_by_email(email="test@example.com")
        self.orders.request.make_request.assert_called_with('getOrdersByEmail', email="test@example.com")
        self.assertTrue(result["success"])

    def test_get_orders_by_phone(self):
        result = self.orders.get_orders_by_phone(phone="123456789")
        self.orders.request.make_request.assert_called_with('getOrdersByPhone', phone="123456789")
        self.assertTrue(result["success"])

    def test_add_invoice(self):
        result = self.orders.add_invoice(order_id=123, series_id=1)
        self.orders.request.make_request.assert_called_with('addInvoice', order_id=123, series_id=1)
        self.assertTrue(result["success"])

    def test_get_invoices(self):
        result = self.orders.get_invoices(invoice_id=1, order_id=123, date_from=987654321, id_from=1, series_id=2,
                                          get_external_invoices=True)
        self.orders.request.make_request.assert_called_with('getInvoices', invoice_id=1, order_id=123,
                                                            date_from=987654321,
                                                            id_from=1, series_id=2, get_external_invoices=True)
        self.assertTrue(result["success"])

    def test_get_series(self):
        result = self.orders.get_series()
        self.orders.request.make_request.assert_called_with('getSeries')
        self.assertTrue(result["success"])

    def test_get_order_status_list(self):
        result = self.orders.get_order_status_list()
        self.orders.request.make_request.assert_called_with('getOrderStatusList')
        self.assertTrue(result["success"])

    def test_get_order_payments_history(self):
        result = self.orders.get_order_payments_history(order_id=123, show_full_history=True)
        self.orders.request.make_request.assert_called_with('getOrderPaymentsHistory', order_id=123,
                                                            show_full_history=True)
        self.assertTrue(result["success"])

    def test_get_new_receipts(self):
        result = self.orders.get_new_receipts(series_id=1)
        self.orders.request.make_request.assert_called_with('getNewReceipts', series_id=1)
        self.assertTrue(result["success"])

    def test_get_receipt(self):
        result = self.orders.get_receipt(receipt_id=1, order_id=None)
        self.orders.request.make_request.assert_called_with('getReceipt', receipt_id=1, order_id=None)
        self.assertTrue(result["success"])

    def test_set_order_fields(self):
        result = self.orders.set_order_fields(order_id=123, admin_comments="Admin comments",
                                              user_comments="User comments",
                                              payment_method="Credit Card", payment_method_cod=None, email=None,
                                              phone=None,
                                              user_login=None, delivery_method=None, delivery_price=None,
                                              delivery_fullname=None, delivery_company=None, delivery_address=None,
                                              delivery_postcode=None, delivery_city=None, delivery_country_code=None,
                                              delivery_point_id=None, delivery_point_name=None,
                                              delivery_point_address=None,
                                              delivery_point_postcode=None, delivery_point_city=None,
                                              invoice_fullname=None,
                                              invoice_company=None, invoice_nip=None, invoice_address=None,
                                              invoice_postcode=None,
                                              invoice_city=None, invoice_country_code=None, want_invoice=None,
                                              extra_field_1=None, extra_field_2=None, pick_state=None, pack_state=None)
        self.orders.request.make_request.assert_called_with('setOrderFields', order_id=123,
                                                            admin_comments="Admin comments",
                                                            user_comments="User comments",
                                                            payment_method="Credit Card", payment_method_cod=None,
                                                            email=None, phone=None,
                                                            user_login=None, delivery_method=None, delivery_price=None,
                                                            delivery_fullname=None, delivery_company=None,
                                                            delivery_address=None,
                                                            delivery_postcode=None, delivery_city=None,
                                                            delivery_country_code=None,
                                                            delivery_point_id=None, delivery_point_name=None,
                                                            delivery_point_address=None,
                                                            delivery_point_postcode=None, delivery_point_city=None,
                                                            invoice_fullname=None,
                                                            invoice_company=None, invoice_nip=None,
                                                            invoice_address=None, invoice_postcode=None,
                                                            invoice_city=None, invoice_country_code=None,
                                                            want_invoice=None,
                                                            extra_field_1=None, extra_field_2=None, pick_state=None,
                                                            pack_state=None)
        self.assertTrue(result["success"])

    def test_add_order_product(self):
        result = self.orders.add_order_product(order_id=123, storage="shop", storage_id="store123", product_id="ABC123",
                                               name="Product A", price_brutto=10.99, quantity=2)
        self.orders.request.make_request.assert_called_with('addOrderProduct', order_id=123, storage="shop",
                                                            storage_id="store123",
                                                            product_id="ABC123", variant_id=None, auction_id=None,
                                                            name="Product A", sku=None,
                                                            ean=None, attributes=None, price_brutto=10.99,
                                                            tax_rate=None, quantity=2, weight=None)
        self.assertTrue(result["success"])

    def test_set_order_product_fields(self):
        result = self.orders.set_order_product_fields(order_id=123, order_product_id=456, name='Updated Product A',
                                                      price_brutto=12.99)
        self.orders.request.make_request.assert_called_with('setOrderProductFields', order_id=123, order_product_id=456,
                                                            storage=None, storage_id=None, product_id=None,
                                                            variant_id=None, auction_id=None,
                                                            name='Updated Product A', sku=None, ean=None,
                                                            attributes=None, price_brutto=12.99,
                                                            tax_rate=None, quantity=None, weight=None)
        self.assertTrue(result["success"])

    def test_delete_order_product(self):
        result = self.orders.delete_order_product(order_id=123, order_product_id=456)
        self.orders.request.make_request.assert_called_with('deleteOrderProduct', order_id=123, order_product_id=456)
        self.assertTrue(result["success"])

    def test_set_order_payment(self):
        result = self.orders.set_order_payment(order_id=123, payment_done=20.0, payment_date=987654321,
                                               payment_comment="Payment received")
        self.orders.request.make_request.assert_called_with('setOrderPayment', order_id=123, payment_done=20.0,
                                                            payment_date=987654321, payment_comment="Payment received")
        self.assertTrue(result["success"])

    def test_set_order_status(self):
        result = self.orders.set_order_status(order_id=123, status_id=2)
        self.orders.request.make_request.assert_called_with('setOrderStatus', order_id=123, status_id=2)
        self.assertTrue(result["success"])

    def test_set_order_receipt(self):
        result = self.orders.set_order_receipt(receipt_id=1, receipt_nr="R123", date=987654321, printer_error=False)
        self.orders.request.make_request.assert_called_with('setOrderReceipt', receipt_id=1, receipt_nr="R123",
                                                            date=987654321, printer_error=False)
        self.assertTrue(result["success"])

    def test_add_order_invoice_file(self):
        result = self.orders.add_order_invoice_file(invoice_id=1, file="base64_encoded_file",
                                                    external_invoice_number="INV001")
        self.orders.request.make_request.assert_called_with('addOrderInvoiceFile', invoice_id=1,
                                                            file="base64_encoded_file",
                                                            external_invoice_number="INV001")
        self.assertTrue(result["success"])
