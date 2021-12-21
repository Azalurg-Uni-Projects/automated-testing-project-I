import unittest
from src.gra import Game


class Game_test(unittest.TestCase):

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

    def test_check_init_val_player1(self):
        self.assertEqual(self.game.player1_name, "Jacek")

    def test_check_init_val_player2(self):
        self.assertEqual(self.game.player2_name, "Wojtas")

    def test_change_player_success(self):
        self.game.change_player()
        self.assertEqual(self.game.next, 2)

    def test_change_player_success2(self):
        self.game.change_player()
        self.game.change_player()
        self.assertEqual(self.game.next, 1)

    def test_move1(self):
        self.assertEqual(self.game.move(1), [
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0]])

    def test_move2(self):
        self.game.move(7)
        self.assertEqual(self.game.move(1), [
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0],
                        [2, 0, 0, 0, 0, 0, 1]])

    def test_move_full(self):
        self.game.move(1)   # p1
        self.game.move(1)   # p2

        self.game.move(1)  # p1
        self.game.move(1)  # p2

        self.game.move(1)  # p1
        self.game.move(1)  # p2

        self.assertEqual(self.game.move(1), [
                        [2, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0],
                        [2, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0],
                        [2, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0]])

    def test_move_string(self):
        self.assertEqual(self.game.move("1"), self.empty_board)

    def test_move_array(self):
        self.assertEqual(self.game.move([]), self.empty_board)

    def test_move_dic(self):
        self.assertEqual(self.game.move({}), self.empty_board)

    def test_move_tuple(self):
        self.assertEqual(self.game.move(()), self.empty_board)

    def test_move_none(self):
        self.assertEqual(self.game.move(None), self.empty_board)

    def test_move_wrong_range1(self):
        self.assertEqual(self.game.move(0), self.empty_board)

    def test_move_wrong_range2(self):
        self.assertEqual(self.game.move(8), self.empty_board)

    def test_move_back1(self):
        self.game.move(1)
        self.assertEqual(self.game.move_back(), self.empty_board)

    def tearDown(self):
        self.game = None
