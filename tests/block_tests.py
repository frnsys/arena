import arena
import unittest
from arena.blocks import Block
from arena.channels import Channel


class BlockTests(unittest.TestCase):
    def test_data(self):
        block = Block('896296')
        self.assertEqual(block.title, 'WELCOME TO THE BURRITO GALAXY WEBZONE')
        self.assertEqual(block.source['url'], 'http://burritogalaxy.com/')

    def test_channels(self):
        block = Block('896296')
        chans, page = block.channels()
        self.assertTrue(len(chans) > 0)
        for chan in chans:
            self.assertIsInstance(chan, Channel)

    def test_search(self):
        results, page = arena.blocks.search('BURRITO GALAXY')
        self.assertTrue(len(results) > 0)
        for block in results:
            self.assertIsInstance(block, Block)
