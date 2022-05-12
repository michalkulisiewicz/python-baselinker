import json
import requests


class Request:

    def __init__(self, api_token):
        self.api_url = 'https://api.baselinker.com/connector.php'
        self.api_token = api_token

    def __get_request_data(self, method_name, parameters=None):
        request_data = {'method': method_name}
        if parameters:
            request_data['parameters'] = json.dumps(parameters)
        return request_data

    def __get_request_headers(self):
        headers = {'X-BLToken': self.api_token}
        return headers

    def make_request(self, method_name, **kwargs):
        requests_data = self.__get_request_data(method_name, kwargs)
        headers = self.__get_request_headers()
        try:
            with requests.Session() as s:
                response = s.post(self.api_url, data=requests_data, headers=headers)
                content = json.loads(response.content.decode("utf-8"))
                return content

        except requests.RequestException as e:
            print(e)
            raise e
