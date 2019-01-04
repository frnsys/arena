import requests
from urllib.parse import urlencode


class Auth:
    def __init__(self, client_id, client_secret, callback_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.callback_url = callback_url

    def request_url(self):
        """This redirects users to {callback_url}/?code=CODE"""
        params = {
            'client_id': self.client_id,
            'redirect_uri': self.callback_url,
            'response_type': 'code'
        }
        query_str = urlencode(params)
        return 'https://dev.are.na/oauth/authorize?{}'.format(query_str)

    def request_access_token(self, code):
        resp = requests.post('https://dev.are.na/oauth/token', params={
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.callback_url,
            'code': code,
            'grant_type': 'authorization_code'
        })
        return resp.json()
