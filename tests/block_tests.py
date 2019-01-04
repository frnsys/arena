import os
import unittest
from arena import Arena
from arena.blocks import Block
from arena.channels import Channel

token = os.environ['ARENA']
arena = Arena(token)

class BlockTests(unittest.TestCase):
    def test_data(self):
        block = arena.blocks.block('896296')
        self.assertEqual(block.title, 'WELCOME TO THE BURRITO GALAXY WEBZONE')
        self.assertEqual(block.source['url'], 'http://burritogalaxy.com/')

    def test_channels(self):
        block = arena.blocks.block('896296')
        chans, page = block.channels()
        print(chans)
        self.assertTrue(len(chans) > 0)
        for chan in chans:
            self.assertIsInstance(chan, Channel)

    def test_search(self):
        results, page = arena.blocks.search('BURRITO GALAXY')
        self.assertTrue(len(results) > 0)
        for block in results:
            self.assertIsInstance(block, Block)
