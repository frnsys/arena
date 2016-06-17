from .search import Search
from .resource import Resource, paginated


class User(Resource):
    base_endpoint = '/users'

    def __init__(self, id, access_token):
        self.id = id
        self.access_token = access_token
        data = self._get('/{}'.format(id))
        for name, val in data.items():
            setattr(self, name, val)

    def channel(self):
        """get the user's channel"""
        return self._get('/{}/channel'.format(self.id), auth=True)

    def channels(self):
        """get the user's channels"""
        return self._get('/{}/channels'.format(self.id), auth=True)

    def following(self):
        """get who/what the user is following"""
        return self._get('/{}/following'.format(self.id), auth=True)

    def followers(self):
        """get the user's followers"""
        return self._get('/{}/followers'.format(self.id), auth=True)


class Users(Resource):
    base_endpoint = '/users'

    def user(self, id):
        """get an existing user"""
        return User(id, access_token=self.access_token)

    @paginated
    def search(self, query, **kwargs):
        return Search().users(query, **kwargs)
