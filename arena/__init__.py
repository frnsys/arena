BASE_URL = 'http://api.are.na/v2'

from .feed import Feed
from .users import Users
from .blocks import Blocks
from .channels import Channels
from .search import Search
from .auth import Auth


class Arena:
    def __init__(self, access_token):
        self.access_token = access_token

        self.users = Users(self)
        self.blocks = Blocks(self)
        self.channels = Channels(self)
        self.feed = Feed(self)
        self.search = Search(self)
