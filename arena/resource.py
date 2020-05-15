import requests
from functools import wraps
from arena import BASE_URL


def paginated(fn):
    @wraps(fn)
    def decorated(*args, **kwargs):
        params = {
            'page': kwargs.pop('page', 1),
            'per': kwargs.pop('per_page', 20)
        }
        params.update(kwargs.get('params', {}))
        kwargs['params'] = params
        return fn(*args, **kwargs)
    return decorated


class Resource():
    def __init__(self, api):
        self.api = api

    def _set_data(self, data):
        self.data = data
        for name, val in data.items():
            setattr(self, name, val)

    def _headers(self, auth):
        if auth:
            if self.api.access_token is not None:
                return {
                    'Authorization': 'Bearer {}'.format(self.api.access_token)
                }
            elif self.api.auth_token is not None:
                return {
                    'X-AUTH-TOKEN': self.api.auth_token
                }
            raise AttributeError('No access token or auth token is set')
        return {}

    def _url(self, endpoint):
        endpoint = endpoint.format(**self.__dict__)
        return ''.join([BASE_URL, self.base_endpoint, endpoint])

    def _get(self, endpoint, params=None, auth=False):
        resp = requests.get(
            self._url(endpoint),
            params=params or {},
            headers=self._headers(auth))
        if resp.status_code != 200:
            resp.raise_for_status()
        return resp.json()

    def _post(self, endpoint, data, params=None):
        resp = requests.post(
            self._url(endpoint),
            params=params or {},
            headers=self._headers(True),
            json=data)
        if resp.status_code != 200:
            resp.raise_for_status()
        return resp.json()

    def _put(self, endpoint, data=None, params=None):
        data = data or {}
        resp = requests.put(
            self._url(endpoint),
            params=params or {},
            headers=self._headers(True),
            json=data)

        # 204 No Content
        if resp.status_code == 204:
            return
        elif resp.status_code != 200:
            resp.raise_for_status()

        return resp.json()

    def _delete(self, endpoint, params=None):
        resp = requests.delete(
            self._url(endpoint),
            params=params or {},
            headers=self._headers(True))

        # 204 No Content
        if resp.status_code == 204:
            return
        elif resp.status_code != 200:
            resp.raise_for_status()

        return resp.json()

    def _resource(self, resource_cls, *args, **kwargs):
        return resource_cls(self.api, *args, **kwargs)

    def _from_data(self, data):
        subclasses = Resource.__subclasses__()
        cls_name = data['base_class']
        try:
            cls = next(cls for cls in subclasses if cls.__name__ == cls_name)
            obj = self._resource(cls, **data)
        except StopIteration:
            raise TypeError('Unknown base_class: "{}"'.format(cls))
        return obj
