from .resource import Resource


class Feed(Resource):
    base_endpoint = '/feed'

    def __call__(self, offset=0):
        page = self._get('', params={'offset': offset}, auth=True)
        items = [self._from_data(d) for d in page.pop('items')]
        return items, page
