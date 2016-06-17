import requests
from functools import wraps

BASE_URL = 'http://api.are.na/v2'


def paginated(fn):
    @wraps(fn)
    def decorated(*args, page=0, per_page=15, **kwargs):
        params = kwargs.get('params', {})
        params.update({
            'page': page,
            'per': per_page})
        kwargs['params'] = params
        return fn(*args, **kwargs)
    return decorated


class Resource():
    def __init__(self, access_token=None):
        self.access_token = access_token

    def _headers(self, auth):
        if auth:
            if self.access_token is not None:
                return {
                    'Authorization': 'Bearer {}'.format(self.access_token)
                }
            elif self.auth_token is not None:
                return {
                    'X-AUTH-TOKEN': self.auth_token
                }
            raise AttributeError('No access token or auth token is set')
        return {}

    def _get(self, endpoint, params=None, auth=False):
        resp = requests.get(
            ''.join([BASE_URL, self.base_endpoint, endpoint]),
            params=params or {},
            headers=self._headers(auth))
        if resp.status_code != 200:
            resp.raise_for_status()
        return resp.json()

    def _post(self, endpoint, data, params=None):
        resp = requests.post(
            ''.join([BASE_URL, self.base_endpoint, endpoint]),
            params=params or {},
            headers=self._headers(True),
            json=data)
        if resp.status_code != 200:
            resp.raise_for_status()
        return resp.json()

    def _put(self, endpoint, data, params=None):
        resp = requests.put(
            ''.join([BASE_URL, self.base_endpoint, endpoint]),
            params=params or {},
            headers=self._headers(True),
            json=data)
        if resp.status_code != 200:
            resp.raise_for_status()
        return resp.json()

    def _delete(self, endpoint, params=None):
        resp = requests.delete(
            ''.join([BASE_URL, self.base_endpoint, endpoint]),
            params=params or {},
            headers=self._headers(True))
        if resp.status_code != 200:
            resp.raise_for_status()
        return resp.json()
