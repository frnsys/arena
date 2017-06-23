from arena.search import search
from arena.channels import Channel
from arena.resource import Resource, paginated, resource_for_data


class User(Resource):
    base_endpoint = '/users'

    def __init__(self, id, **data):
        self.id = id
        if not data:
            data = self._get('/{id}')
        self._set_data(data)

    def channel(self):
        """get the user's channel"""
        data = self._get('/{id}/channel', auth=True)
        return Channel(**data)

    def channels(self):
        """get the user's channels"""
        page = self._get('/{id}/channels', auth=True)
        chans = [Channel(**d) for d in page.pop('channels')]
        return chans, page

    def following(self):
        """get who/what the user is following"""
        page = self._get('/{id}/following', auth=True)
        items = [resource_for_data(d) for d in page.pop('following')]
        return items, page

    def followers(self):
        """get the user's followers"""
        page = self._get('/{id}/followers', auth=True)
        users = [User(**d) for d in page.pop('users')]
        return users, page


class Users(Resource):
    base_endpoint = '/users'

    def user(self, id):
        """get an existing user"""
        return User(id)

    @paginated
    def search(self, query, **kwargs):
        """searches users"""
        page = search.users(query, **kwargs)
        for k in ['channels', 'blocks']:
            page.pop(k)
        users = [User(**d) for d in page.pop('users')]
        return users, page
