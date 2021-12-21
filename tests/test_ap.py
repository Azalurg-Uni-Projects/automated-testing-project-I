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

    def test_init_board(self):
        assert_that(self.game.board).is_equal_to(self.empty_board)

    def test_iterable(self):
        assert_that(self.game.move(1)).is_iterable()

    def test_type_of(self):
        assert_that(self.game.move(1)).is_type_of(list)

    def test_is_not_none(self):
        self.game.board = self.winning_board
        self.game.check_board()
        assert_that(self.game.winner).is_not_none()

    def tearDown(self):
        self.game = None
