import unittest
import requests
from unittest.mock import patch
from baselinker import Request


class TestRequest(unittest.TestCase):

    def setUp(self):
        self.api_token = 'my_token'
        self.request = Request(api_token=self.api_token)

    def test_init_with_valid_api_token(self):
        request = Request(api_token=self.api_token)
        self.assertEqual(request.api_token, self.api_token)
        self.assertEqual(request.api_url, 'https://api.baselinker.com/connector.php')

    def test_init_with_empty_api_token(self):
        with self.assertRaises(ValueError):
            Request(api_token='')

    def test_get_request_data_without_parameters(self):
        method_name = 'test_method'
        expected_request_data = {'method': method_name}

        request_data = self.request._Request__get_request_data(method_name)

        self.assertEqual(request_data, expected_request_data)

    def test_get_request_data_with_parameters(self):
        method_name = 'test_method'
        parameters = {'param1': 'value1', 'param2': 'value2'}
        expected_request_data = {'method': method_name, 'parameters': '{"param1": "value1", "param2": "value2"}'}

        request_data = self.request._Request__get_request_data(method_name, parameters)

        self.assertEqual(request_data, expected_request_data)

    def test_get_request_headers(self):
        expected_headers = {'X-BLToken': self.api_token}

        headers = self.request._Request__get_request_headers()

        self.assertEqual(headers, expected_headers)

    @patch('requests.Session.post')
    def test_make_request_success(self, mock_post):
        method_name = 'test_method'
        parameters = {'param1': 'value1', 'param2': 'value2'}
        expected_request_data = {'method': method_name, 'parameters': '{"param1": "value1", "param2": "value2"}'}
        expected_headers = {'X-BLToken': self.api_token}
        expected_response_content = '{"status": "success", "result": "Test Result"}'
        mock_post.return_value.content.decode.return_value = expected_response_content

        response = self.request.make_request(method_name, **parameters)

        mock_post.assert_called_once_with(self.request.api_url, data=expected_request_data, headers=expected_headers)
        self.assertEqual(response, {'status': 'success', 'result': 'Test Result'})

    @patch('requests.Session.post', side_effect=requests.RequestException('Test Error'))
    @patch('builtins.print')
    def test_make_request_failure(self, mock_print, mock_post):
        method_name = 'test_method'
        parameters = {'param1': 'value1', 'param2': 'value2'}

        with self.assertRaises(requests.RequestException):
            self.request.make_request(method_name, **parameters)
