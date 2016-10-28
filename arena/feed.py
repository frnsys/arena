from .resource import Resource


class Feed(Resource):
    base_endpoint = '/feed'

    def __call__(self, offset=0):
        return self._get('', params={'offset': offset}, auth=True)
