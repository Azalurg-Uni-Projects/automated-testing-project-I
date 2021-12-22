import unittest
from assertpy import assert_that
from src.board import Board


class Board_test(unittest.TestCase):
    def setUp(self):
        self.player1_color = 1
        self.player2_color = 2
        self.board = Board()

    def test_instance(self):
        assert_that(self.board).is_instance_of(Board)

    def test_check_board_not_finished(self):
        assert_that(self.board.check_board(self.player1_color, self.player2_color)[0]).is_false()

    def test_init_wrong_rows_val_string(self):
        self.assertRaises(ValueError, Board, "10")

    def test_init_wrong_rows_val_list(self):
        self.assertRaises(ValueError, Board, [])

    def test_init_wrong_rows_val_float(self):
        self.assertRaises(ValueError, Board, 11.11)

    def test_check_board_draw(self):
        self.game.board = [
            [1, 2, 1, 2, 1, 2, 2],
            [1, 2, 1, 2, 1, 2, 1],
            [2, 1, 2, 1, 2, 1, 2],
            [2, 1, 2, 1, 2, 1, 2],
            [1, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1]]
        assert_that(self.board.check_board(self.player1_color, self.player2_color)[0]).is_true()

    def test_check_win_horizontal_player1(self):
        self.game.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [2, 2, 2, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0]]
        assert_that(self.board.check_board(self.player1_color, self.player2_color)[1]).is_equal_to(self.player1_color)

    def test_check_win_horizontal_player2(self):
        self.game.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [2, 2, 2, 2, 0, 0, 0],
            [1, 1, 1, 2, 1, 1, 0]]
        assert_that(self.board.check_board(self.player1_color, self.player2_color)[1]).is_equal_to(self.player2_color)

    def test_check_win_vertical1(self):
        self.game.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0],
            [2, 2, 0, 1, 2, 0, 0],
            [1, 1, 0, 1, 2, 0, 0]]
        assert_that(self.board.check_board(self.player1_color, self.player2_color)[1]).is_equal_to(self.player1_color)

    def test_check_win_vertical2(self):
        self.game.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 1, 2, 0, 0],
            [2, 2, 0, 1, 2, 1, 0],
            [1, 1, 0, 1, 2, 1, 0]]
        assert_that(self.board.check_board(self.player1_color, self.player2_color)[1]).is_equal_to(self.player2_color)

    def test_check_I_slope1(self):
        self.game.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0],
            [0, 1, 1, 2, 0, 0, 0],
            [1, 2, 2, 2, 2, 0, 0]]
        assert_that(self.board.check_board(self.player1_color, self.player2_color)[1]).is_equal_to(self.player1_color)

    def test_check_I_slope2(self):
        self.game.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0],
            [2, 0, 0, 1, 1, 0, 1]]
        assert_that(self.board.check_board(self.player1_color, self.player2_color)[1]).is_equal_to(self.player2_color)

    def test_check_II_slope1(self):
        self.game.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [2, 2, 2, 0, 1, 0, 2]]
        assert_that(self.board.check_board(self.player1_color, self.player2_color)[1]).is_equal_to(self.player1_color)

    def test_check_II_slope2(self):
        self.game.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [1, 1, 1, 0, 2, 0, 1]]
        assert_that(self.board.check_board(self.player1_color, self.player2_color)[1]).is_equal_to(self.player1_color)

    def tearDown(self):
        self.game = None
