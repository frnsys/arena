import unittest
from tests import arena
from arena.channels import Channel


class UserTests(unittest.TestCase):
    def setUp(self):
        self.user = arena.users.user('francis-tseng')

    def test_data(self):
        self.assertEqual(self.user.slug, 'francis-tseng')

    # Endpoint seems to be missing?
    def test_channel(self):
        return

        chan = self.user.channel()
        self.assertIsInstance(chan, Channel)

    def test_channels(self):
        chans, page = self.user.channels()
        self.assertEqual(page['current_page'], 1)
        self.assertGreater(len(chans), 0)

    def test_followers(self):
        users, page = self.user.followers()
        self.assertEqual(page['current_page'], 1)
        self.assertGreater(len(users), 0)

    def test_following(self):
        following, page = self.user.following()
        self.assertEqual(page['current_page'], 1)
        self.assertGreater(len(following), 0)
