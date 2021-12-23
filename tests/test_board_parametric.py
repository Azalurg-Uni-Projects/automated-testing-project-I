import unittest
from parameterized import parameterized, parameterized_class
from src.board import Board
import json


class Board_test_parametric(unittest.TestCase):
    def setUp(self):
        self.player1_color = 1
        self.player2_color = 2
        self.board = Board()
        f = open('data/parametric_test_data.json')
        data = json.load(f)
        f.close()

    def tearDown(self):
        self.board = None
