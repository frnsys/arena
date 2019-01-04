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

    # Getting a 500 error
    def test_update(self):
        return
        chan = arena.channels.channel('arena-api-testing')
        self.assertEqual(chan.status, 'public')

        chan.update(status='closed')
        chan = arena.channels.channel('arena-api-testing')
        self.assertEqual(chan.status, 'closed')

        chan.update(status='public')
        chan = arena.channels.channel('arena-api-testing')
        self.assertEqual(chan.status, 'public')

    # Endpoint seems to be missing?
    def test_toggle_block_selection(self):
        return

        block_id = '896296'
        chan = arena.channels.channel('arena-api-testing')
        contents, _ = chan.contents()

        selected_before = any(c.id == block_id for c in contents if c.base_class == 'Block')
        chan.toggle_selection(block_id)

        contents, _ = chan.contents()
        selected_after = any(c.id == block_id for c in contents if c.base_class == 'Block')

        self.assertNotEqual(selected_before, selected_after)

    def test_add_remove_block(self):
        chan = arena.channels.channel('arena-api-testing')
        block = chan.add_block('https://github.com/frnsys/arena')

        # Check block was added
        contents, _ = chan.contents()
        blocks = [c for c in contents if c.base_class == 'Block']
        self.assertTrue(any(b.id == block.id for b in blocks))

        chan.remove_block(block.id)

        # Check block was removed
        contents, _ = chan.contents()
        blocks = [c for c in contents if c.base_class == 'Block']
        self.assertFalse(any(b.id == block.id for b in blocks))