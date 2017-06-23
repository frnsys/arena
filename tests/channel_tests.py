import unittest
from arena.channels import Channel, Channels


class ChannelTests(unittest.TestCase):
    def setUp(self):
        self.channels = Channels()

    def test_list(self):
        chans, page = self.channels.list()
        self.assertTrue(len(chans) > 0)
        for chan in chans:
            self.assertIsInstance(chan, Channel)

    def test_channel(self):
        chan = self.channels.channel('faq')
        self.assertEqual(chan.slug, 'faq')