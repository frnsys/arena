import os
import unittest
from arena import Arena

token = os.environ['ARENA']
arena = Arena(token)

class UserTests(unittest.TestCase):
    def setUp(self):
        self.user = arena.users.user('francis-tseng')

    def test_data(self):
        self.assertEqual(self.user.slug, 'francis-tseng')
