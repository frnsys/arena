from arena.search import search
from arena.resource import Resource, paginated


class Block(Resource):
    base_endpoint = '/blocks'

    def __init__(self, id):
        self.id = id
        data = self._get('/{}'.format(id))
        self._set_data(data)

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
        return Block(id)

    @paginated
    def search(self, query, **kwargs):
        """searches blocks"""
        return search.blocks(query, **kwargs)
