auth_token = None
access_token = None
BASE_URL = 'http://api.are.na/v2'

from .feed import Feed
from .users import Users, User
from .blocks import Blocks, Block
from .channels import Channels, Channel

users = Users()
blocks = Blocks()
channels = Channels()
feed = Feed()
