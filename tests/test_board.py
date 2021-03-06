import unittest
from assertpy import *
from src.board import Board


def check_board_params(self):
    rows = self.val.rows
    columns = self.val.columns
    separator = self.val.separator
    board = self.val.board
    good_board = [[separator for i in range(columns)] for j in range(rows)]
    if type(rows) is not int:
        self.error("Rows wrong type")
    elif type(columns) is not int:
        self.error("Columns wrong type")
    elif rows < 4:
        self.error("Rows too small")
    elif columns < 4:
        self.error("Columns too small")
    if board != good_board:
        self.error("Wrong board")
    return self


add_extension(check_board_params)


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

    def test_init_wrong_rows_val_dic(self):
        self.assertRaises(ValueError, Board, {})

    def test_init_wrong_rows_val_none(self):
        self.assertRaises(ValueError, Board, None)

    def test_init_wrong_rows_val_too_small(self):
        self.assertRaises(Exception, Board, 3)

    def test_init_wrong_columns_val_string(self):
        self.assertRaises(ValueError, Board, 10, "10")

    def test_init_wrong_columns_val_list(self):
        self.assertRaises(ValueError, Board, 10, [])

    def test_init_wrong_columns_val_float(self):
        self.assertRaises(ValueError, Board, 10, 11.11)

    def test_init_wrong_columns_val_dic(self):
        self.assertRaises(ValueError, Board, 10, {})

    def test_init_wrong_columns_val_none(self):
        self.assertRaises(ValueError, Board, 10, None)

    def test_init_wrong_columns_val_too_small(self):
        self.assertRaises(Exception, Board, 10, 3)

    def test_check_board_draw(self):
        self.board.board = [
            [1, 2, 1, 2, 1, 2, 2],
            [1, 2, 1, 2, 1, 2, 1],
            [2, 1, 2, 1, 2, 1, 2],
            [2, 1, 2, 1, 2, 1, 2],
            [1, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1]]
        assert_that(self.board.check_board(self.player1_color, self.player2_color)[0]).is_true()

    def test_check_win_horizontal_player1(self):
        self.board.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [2, 2, 2, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0]]
        assert_that(self.board.check_board(self.player1_color, self.player2_color)[1]).is_equal_to(self.player1_color)

    def test_check_win_horizontal_player2(self):
        self.board.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [2, 2, 2, 2, 0, 0, 0],
            [1, 1, 1, 2, 1, 1, 0]]
        assert_that(self.board.check_board(self.player1_color, self.player2_color)[1]).is_equal_to(self.player2_color)

    def test_check_win_vertical1(self):
        self.board.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0],
            [2, 2, 0, 1, 2, 0, 0],
            [1, 1, 0, 1, 2, 0, 0]]
        assert_that(self.board.check_board(self.player1_color, self.player2_color)[1]).is_equal_to(self.player1_color)

    def test_check_win_vertical2(self):
        self.board.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0],
            [0, 0, 0, 1, 2, 0, 0],
            [2, 2, 0, 1, 2, 1, 0],
            [1, 1, 0, 1, 2, 1, 0]]
        assert_that(self.board.check_board(self.player1_color, self.player2_color)[1]).is_equal_to(self.player2_color)

    def test_check_I_slope1(self):
        self.board.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0],
            [0, 1, 1, 2, 0, 0, 0],
            [1, 2, 2, 2, 0, 0, 0]]
        assert_that(self.board.check_board(self.player1_color, self.player2_color)[1]).is_equal_to(self.player1_color)

    def test_check_I_slope2(self):
        self.board.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0],
            [2, 0, 0, 1, 1, 0, 1]]
        assert_that(self.board.check_board(self.player1_color, self.player2_color)[1]).is_equal_to(self.player2_color)

    def test_check_II_slope1(self):
        self.board.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [2, 2, 2, 0, 1, 0, 2]]
        assert_that(self.board.check_board(self.player1_color, self.player2_color)[1]).is_equal_to(self.player1_color)

    def test_check_II_slope2(self):
        self.board.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [1, 1, 1, 0, 2, 0, 1]]
        assert_that(self.board.check_board(self.player1_color, self.player2_color)[1]).is_equal_to(self.player2_color)

    def test_check_correct_return(self):
        self.board.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [1, 1, 1, 0, 2, 0, 1]]
        assert_that(self.board.check_board(self.player1_color, self.player2_color)).is_iterable()

    def test_board_printing(self):
        assert_that(self.board.print_board()).is_same_as(True)

    def test_check_params(self):
        assert_that(self.board).check_board_params()

    def tearDown(self):
        self.board = None
