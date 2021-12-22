import unittest
from hamcrest import *
from src.player import Player


class Player_test(unittest.TestCase):
    def setUp(self):
        self.player = Player("Bob", "green")

    def tearDown(self):
        self.player = None
