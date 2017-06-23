import arena
import unittest
from config import token
from arena.channels import Channels

arena.access_token = token

class TestChannels(unittest.TestCase):
    def setUp(self):
        self.channels = Channels()

    def test_list(self):
        data = self.channels.list()
        self.assertTrue(data is not None)

    def test_channel(self):
        data = self.channels.channel('faq')
        self.assertTrue(data is not None) # TODO better tests