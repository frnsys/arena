import unittest
from arena.users import User


class UserTests(unittest.TestCase):
    def setUp(self):
        self.user = User('francis-tseng')

    def test_data(self):
        self.assertEqual(self.user.slug, 'francis-tseng')
