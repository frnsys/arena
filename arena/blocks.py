from .search import Search
from .resource import Resource, paginated


class Block(Resource):
    base_endpoint = '/blocks'

    def __init__(self, id, access_token):
        self.id = id
        self.access_token = access_token
        data = self._get('/{}'.format(id))
        for name, val in data.items():
            setattr(self, name, val)

    @paginated
    def channels(self, **kwargs):
        """get channels this block is in"""
        return self._get('/{}/channels'.format(self.id), params=kwargs['params'])

    def update(self, **kwargs):
        """update the block's attributes (all are optional):
        - title: str
        - description: markdown
        - content: markdown (for text blocks only)
        """
        return self._put('/{}'.format(self.id), data=kwargs)

    def delete(self):
        """deletes the block"""
        return self._delete('/{}'.format(self.id))


class Blocks(Resource):
    base_endpoint = '/blocks'

    def block(self, id):
        """get an existing block"""
        return Block(id, access_token=self.access_token)

    @paginated
    def search(self, query, **kwargs):
        return Search().blocks(query, **kwargs)
