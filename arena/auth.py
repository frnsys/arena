import requests


class Auth:
    def __init__(self, client_id, client_secret, callback_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.callback_url = callback_url

    def request_code(self):
        """This redirects users to {callback_url}/?code=CODE"""
        return requests.get('https://dev.are.na/oauth/authorize', params={
            'client_id': self.client_id,
            'redirect_uri': self.callback_url,
            'response_type': 'code'
        })

    def request_access_token(self, code):
        resp = requests.post('https://dev.are.na/oauth/token', params={
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.callback_url,
            'code': code,
            'grant_type': 'authorization_code'
        })
        return resp.json()
