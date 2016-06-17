from .search import Search
from .resource import Resource, paginated


class Channel(Resource):
    base_endpoint = '/channels'

    def __init__(self, slug, access_token):
        self.slug = slug
        self.access_token = access_token

    @paginated
    def all(self, **kwargs):
        """gets full representation of this channel (paginated)"""
        return self._get('/{}'.format(self.slug), params=kwargs['params'])

    def thumb(self, **kwargs):
        """gets a small representation of this channel"""
        return self._get('/{}/thumb'.format(self.slug))

    @paginated
    def connections(self, **kwargs):
        """get connections for this channel (paginated)"""
        return self._get('/{}/connections'.format(self.slug), params=kwargs['params'])

    @paginated
    def channels(self, **kwargs):
        """get connected channels for this channel (paginated)"""
        return self._get('/{}/channels'.format(self.slug), params=kwargs['params'])

    @paginated
    def contents(self, **kwargs):
        """get only contents for this channel (paginated)"""
        return self._get('/{}/contents'.format(self.slug), params=kwargs['params'])

    def collaborators(self):
        """get only collaborators for this channel"""
        return self._get('/{}/collaborators'.format(self.slug))

    # TODO
    # <http://dev.are.na/documentation/channels#block_45048>
    # def add_collaborator(self):
        # return self._post('{}/collaborators'.format(self.slug)

    def update(self, **kwargs):
        """update a channel's attributes
        can specify:
        - title: str
        - status: one of ['public', 'closed', 'private']
        """
        return self._put('/{}'.format(self.slug), data=kwargs)

    def delete(self):
        """deletes a channel"""
        return self._delete('/{}'.format(self.slug))

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
        return self._post('/{}/blocks'.format(self.slug), data=data)


class Channels(Resource):
    base_endpoint = '/channels'

    @paginated
    def list(self, **kwargs):
        """list channels (paginated)"""
        return self._get('', params=kwargs['params'])

    def create(self, title, status='public'):
        """creates a new channel"""
        return self._post('', data={
            'title': title,
            'status': status
        })

    def channel(self, slug):
        """get an existing channel"""
        return Channel(slug, access_token=self.access_token)

    @paginated
    def search(self, query, **kwargs):
        return Search().channels(query, **kwargs)
