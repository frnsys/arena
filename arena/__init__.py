from .feed import Feed
from .users import Users
from .blocks import Blocks
from .search import Search
from .channels import Channels


class Arena():
    def __init__(self, access_token):
        self.access_token = access_token
        self.users = Users(access_token=access_token)
        self.blocks = Blocks(access_token=access_token)
        self.channels = Channels(access_token=access_token)
        self.feed = Feed(access_token=access_token)
        self.search = Search()
