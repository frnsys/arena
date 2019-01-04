from .resource import Resource, paginated


class Channel(Resource):
    base_endpoint = '/channels'

    def __init__(self, api, slug, **data):
        super().__init__(api)
        self.slug = slug
        if not data:
            data = self.thumb()

        # to not override the `contents` method
        self._contents = data.pop('contents')

        self._set_data(data)
        self.user = self.api.users.user(**self.user)

    @paginated
    def all(self, **kwargs):
        """gets full representation of this channel (paginated)"""
        return self._get('/{slug}', params=kwargs['params'])

    def thumb(self, **kwargs):
        """gets a small representation of this channel"""
        return self._get('/{slug}/thumb', auth=True)

    @paginated
    def connections(self, **kwargs):
        """get connections for this channel (paginated)"""
        page = self._get('/{slug}/connections', params=kwargs['params'])
        chans = [self._resource(Channel, **d) for d in page.pop('channels')]
        return chans, page

    @paginated
    def channels(self, **kwargs):
        """get connected channels for this channel (paginated)"""
        page = self._get('/{slug}/channels', params=kwargs['params'])
        chans = [self._resource(Channel, **d) for d in page.pop('channels')]
        return chans, page

    @paginated
    def contents(self, **kwargs):
        """get only contents for this channel (paginated)"""
        # for some reason this one is missing pagination data?
        page = self._get('/{slug}/contents', params=kwargs['params'])
        contents = [self._from_data(d) for d in page.pop('contents')]
        return contents, page

    def collaborators(self):
        """get only collaborators for this channel"""
        page = self._get('/{slug}/collaborators')
        users = [self.api.users.user(**d) for d in page.pop('users')]
        return users, page

    def add_collaborator(self, collaborator_ids):
        """adds collaborators from the specified
        list of collaborator ids"""
        return self._post('/{slug}/collaborators', data={
            'ids': collaborator_ids
        })

    def set_collaborators(self, collaborator_ids):
        """updates the channel collaborators
        to match the specified list of collaborator ids"""
        return self._post('/{slug}/collaborators', data={
            'ids': collaborator_ids
        })

    # TODO getting a 500 error
    def update(self, **kwargs):
        """update a channel's attributes
        can specify:
        - title: str
        - status: one of ['public', 'closed', 'private']
        """
        return self._put('/{slug}', data=kwargs)

    def delete(self):
        """deletes a channel"""
        return self._delete('/{slug}')

    def sort(self, content_ids):
        """updates the channel order to match the
        order of provided ids"""
        return self._put('/{slug}/sort', data={
            'ids': content_ids
        })

    def add_block(self, source=None, content=None):
        """add a new block to the channel.
        one of `source` or `content` must be specified:
        - source: a url
        - content: github-flavored markdown
        """
        if source is not None:
            data = {'source': source}
        elif content is not None:
            data = {'content': content}
        else:
            raise ValueError('One of `source` or `content` must be specified')
        data = self._post('/{slug}/blocks', data=data)
        return self.api.blocks.block(**data)

    def remove_block(self, block_id):
        """removes a block from the channel"""
        return self._delete('/{{slug}}/blocks/{0}'.format(block_id))

    # TODO This endpoint seems to be broken?
    def toggle_selection(self, block_id):
        """toggle's a block's selection/connection
        to the channel"""
        return self._put('/{{slug}}/blocks/{0}/selection'.format(block_id))


class Channels(Resource):
    base_endpoint = '/channels'

    @paginated
    def list(self, **kwargs):
        """list channels (paginated)"""
        page = self._get('', params=kwargs['params'])
        for k in ['users', 'blocks']:
            page.pop(k)
        chans = [self._resource(Channel, **d)
                 for d in page.pop('channels')]
        return chans, page

    def create(self, title, status='public'):
        """creates a new channel"""
        return self._post('', data={
            'title': title,
            'status': status
        })

    def channel(self, *args, **kwargs):
        """get an existing channel"""
        return self._resource(Channel, *args, **kwargs)

    @paginated
    def search(self, query, **kwargs):
        """searches channels"""
        page = self.api.search.channels(query, **kwargs)
        for k in ['users', 'blocks']:
            page.pop(k)
        chans = [self._resource(Channel, **d)
                 for d in page.pop('channels')]
        return chans, page
