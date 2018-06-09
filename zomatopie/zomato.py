import os
import requests

zomato_api_url = 'https://developers.zomato.com/api/v2.1/'

class ZomatoAPIRequest():
    """
        Main class responsible for issuing requests to Zomato API
    """

    # shorthand for zomato_api_url
    url = zomato_api_url

    def __init__(self, key=None):
        # access_key is necessary for issuing requests to Zomato
        if key is not None:
            self.key = key
        else:
            if 'ZOMATO_KEY' not in os.environ:
                raise Error

            self.key = os.environ.get('ZOMATO_KEY')

        # response is always json
        # also access_key needs to be sent in headers
        self.headers = {
            'user-agent': 'zomatopie',               # For some reason, zomato API crashes with default user-agent of requests
            'Accept': 'application/json',
            'user-key': self.key
        }

    def make_request(self, path, query_params=None):
        resp = requests.get(
            self.url+path,
            params=query_params,
            headers=self.headers
        )


        if resp.status_code != 200:
            raise resp.raise_for_status()

        # maybe raise a custom exception here?
        self.response = resp.json()
