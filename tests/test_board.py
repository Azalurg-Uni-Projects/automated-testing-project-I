import unittest
from assertpy import assert_that
from src.board import Board


class Board_test(unittest.TestCase):
    def setUp(self):
        self.board = Board(10, 10)
        self.empty_board = [[0 for i in range(10)] for j in range(10)]

    def test_instance(self):
        assert_that(self.board).is_instance_of(Board)

    def tearDown(self):
        self.game = None
