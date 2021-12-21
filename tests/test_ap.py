import unittest
from assertpy import assert_that
from src.gra import Game


class Game_assertpy_test(unittest.TestCase):
    def setUp(self):
        game = Game("Jacek", "Wojtas")
        self.game = game
        self.empty_board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]
        self.winning_board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 2, 1, 0, 0, 0, 0],
            [0, 2, 2, 1, 0, 0, 0],
            [1, 2, 1, 2, 1, 0, 0]]

    def test_instance(self):
        assert_that(self.game).is_instance_of(Game)

    def test_iterable(self):
        assert_that(self.game.move(1)).is_iterable()

    def tearDown(self):
        self.game = None
