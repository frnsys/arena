import unittest
from arena.channels import Channels


class TestChannels(unittest.TestCase):
    def setUp(self):
        self.channels = Channels()

    def test_list(self):
        data = self.channels.list()
        self.assertTrue(data is not None) # TODO better tests

    def test_channel(self):
        data = self.channels.channel('faq')
        self.assertTrue(data is not None) # TODO better tests

    def test_connections(self):
        data = self.channels.connections('arena-influences')
        self.assertTrue(data is not None) # TODO better tests

    def test_connected_channels(self):
        data = self.channels.connections('arena-influences', channels=True)
        self.assertTrue(data is not None) # TODO better tests