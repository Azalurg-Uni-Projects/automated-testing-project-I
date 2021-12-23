import unittest
from parameterized import parameterized, parameterized_class
from src.game import Game


class Game_test_parametric(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def tearDown(self):
        self.game = None
