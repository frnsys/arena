from .users import User
from .channels import Channel
from .resource import Resource, paginated


class Block(Resource):
    base_endpoint = '/blocks'

    def __init__(self, api, id, **data):
        super().__init__(api)
        self.id = id
        if not data:
            data = self._get('/{id}', auth=True)
        self._set_data(data)
        self.user = self._resource(User, **self.user)

    @paginated
    def channels(self, **kwargs):
        """get channels this block is in"""
        page = self._get('/{id}/channels', params=kwargs['params'], auth=True)
        chans = [self._resource(Channel, **d) for d in page.pop('channels')]
        return chans, page

    def update(self, **kwargs):
        """update the block's attributes (all are optional):
        - title: str
        - description: markdown
        - content: markdown (for text blocks only)
        """
        return self._put('/{id}', data=kwargs)


class Blocks(Resource):
    base_endpoint = '/blocks'

    def block(self, *args, **kwargs):
        """get an existing block"""
        return self._resource(Block, *args, **kwargs)

    @paginated
    def search(self, query, **kwargs):
        """searches blocks"""
        page = self.api.search.blocks(query, **kwargs)
        for k in ['channels', 'users']:
            page.pop(k)
        blocks = [self._resource(Block, **d) for d in page.pop('blocks')]
        return blocks, page

