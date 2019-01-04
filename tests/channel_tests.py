import unittest
from tests import arena
from arena.channels import Channel


class ChannelTests(unittest.TestCase):
    def test_list(self):
        chans, page = arena.channels.list()
        self.assertTrue(len(chans) > 0)
        for chan in chans:
            self.assertIsInstance(chan, Channel)

    def test_channel(self):
        chan = arena.channels.channel('yuppie-dystopia')
        self.assertEqual(chan.slug, 'yuppie-dystopia')