import json
import requests


class Request:

    def __init__(self, api_token):
        self.api_url = 'https://api.baselinker.com/connector.php'
        if not api_token:
            raise ValueError('api_key must be set! Obtain key from: https://panel.baselinker.com/other_api_token.php')
        self.api_token = api_token


    def __get_request_data(self, method_name, parameters=None):
        """
        Method that creates body for request
        Keywords:
            method_name (str): (required) Name of the method to invoke.
            parameters (dict): (optional) Dictionary of parameters specified by user.
        Returns:
            request_data(json): Data used inside body of request returned as a json string.
        """
        request_data = {'method': method_name}
        if parameters:
            request_data['parameters'] = json.dumps(parameters)
        return request_data

    def __get_request_headers(self):
        """
        Method that creates request header
        Returns:
            headers(dict): Header needed for request containing api token.
        """
        headers = {'X-BLToken': self.api_token}
        return headers

    def make_request(self, method_name, **kwargs):
        """
        Method that sends request to api endpoint.
        Keywords:
            method_name (str): (required) Name of the method to invoke.
            (**kwargs): (required) Parameters specified by user.
        Returns:
            content(json): Method returns content of the response formatted as json string.
        """
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
