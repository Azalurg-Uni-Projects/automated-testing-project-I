import unittest
from hamcrest import *
from src.player import Player


class Player_test(unittest.TestCase):
    def setUp(self):
        self.player = Player("Bob", "green")

    def test_instance(self):
        assert_that(self.player, instance_of(Player))

    def tearDown(self):
        self.player = None
