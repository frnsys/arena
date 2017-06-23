import arena
from arena.search import search
from arena.resource import Resource, paginated


class Block(Resource):
    base_endpoint = '/blocks'

    def __init__(self, id, **data):
        self.id = id
        if not data:
            data = self._get('/{id}')
        self._set_data(data)
        self.user = arena.User(**self.user)

    @paginated
    def channels(self, **kwargs):
        """get channels this block is in"""
        page = self._get('/{id}/channels', params=kwargs['params'])
        chans = [arena.Channel(**d) for d in page.pop('channels')]
        return chans, page

    def update(self, **kwargs):
        """update the block's attributes (all are optional):
        - title: str
        - description: markdown
        - content: markdown (for text blocks only)
        """
        return self._put('/{id}', data=kwargs)

    def delete(self):
        """deletes the block"""
        return self._delete('/{id}')


class Blocks(Resource):
    base_endpoint = '/blocks'

    def block(self, id):
        """get an existing block"""
        return Block(id)

    @paginated
    def search(self, query, **kwargs):
        """searches blocks"""
        page = search.blocks(query, **kwargs)
        for k in ['channels', 'users']:
            page.pop(k)
        blocks = [Block(**d) for d in page.pop('blocks')]
        return blocks, page

