import unittest
from parameterized import parameterized, parameterized_class
from src.board import Board
import json

f = open('data/parametric_test_data.json')
data = json.load(f)
f.close()


def change_to_tuple(x):
    t = (x, )
    return t


class Board_test_parametric(unittest.TestCase):
    def setUp(self):
        self.player1_color = 1
        self.player2_color = 2
        self.board = Board()

    @parameterized.expand(map(change_to_tuple, data["winning_boards_patterns"]))
    def test_check_board(self, board):
        self.board.board = board
        self.assertTrue(self.board.check_board(self.player1_color, self.player2_color)[0])

    @parameterized.expand(map(change_to_tuple, data["board_size_correct"]))
    def test_init_board_correct(self, value):
        self.assertEqual(Board(value).rows, value)

    @parameterized.expand(map(change_to_tuple, data["board_size_wrong"]))
    def test_init_board_wrong_size(self, value):
        self.assertRaises(Exception, Board, value)

    @parameterized.expand(map(change_to_tuple, data["board_size_not_int"]))
    def test_init_board_wrong_type(self, value):
        self.assertRaises(ValueError, Board, value)

    def tearDown(self):
        self.board = None
