from .resource import Resource, paginated


class User(Resource):
    base_endpoint = '/users'

    def __init__(self, api, id, **data):
        super().__init__(api)
        self.id = id
        if not data:
            data = self._get('/{id}')
        self._set_data(data)

    def channel(self):
        """get the user's channel"""
        data = self._get('/{id}/channel', auth=True)
        return self.api.channels.channel(**data)

    def channels(self):
        """get the user's channels"""
        page = self._get('/{id}/channels', auth=True)
        chans = [self.api.channels.channel(**d) for d in page.pop('channels')]
        return chans, page

    def following(self):
        """get who/what the user is following"""
        page = self._get('/{id}/following', auth=True)
        items = [self._from_data(d) for d in page.pop('following')]
        return items, page

    def followers(self):
        """get the user's followers"""
        page = self._get('/{id}/followers', auth=True)
        users = [self._resource(User, **d) for d in page.pop('users')]
        return users, page


class Users(Resource):
    base_endpoint = '/users'

    def user(self, *args, **kwargs):
        """get an existing user"""
        return self._resource(User, *args, **kwargs)

    @paginated
    def search(self, query, **kwargs):
        """searches users"""
        page = self.api.search.users(query, **kwargs)
        for k in ['channels', 'blocks']:
            page.pop(k)
        users = [self._resource(User, **d) for d in page.pop('users')]
        return users, page
