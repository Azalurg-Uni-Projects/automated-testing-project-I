import unittest
from parameterized import parameterized, parameterized_class
from src.game import Game


class Game_test_parametric(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    @parameterized.expand([([], ), (11.11, ), (None, ), ("3", ), ({}, ), ((), )])
    def test_move_exceptions(self, move):
        self.assertRaises(Exception, self.game.move, move)

    @parameterized.expand([(1,), (2,), (3,), (4,), (5,), (6,), (7, )])
    def test_move_correct(self, move):
        self.assertEqual(type(self.game.move(move)), type([]))

    def tearDown(self):
        self.game = None
