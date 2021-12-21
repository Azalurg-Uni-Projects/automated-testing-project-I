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
        self.winning_board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 2, 1, 0, 0, 0, 0],
            [0, 2, 2, 1, 0, 0, 0],
            [1, 2, 1, 2, 1, 0, 0]]

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

        self.assertRaises(Exception, self.game.move, 1)

    def test_move_string(self):
        self.assertRaises(ValueError, self.game.move, "1")

    def test_move_array(self):
        self.assertRaises(ValueError, self.game.move, [])

    def test_move_dic(self):
        self.assertRaises(ValueError, self.game.move, {})

    def test_move_tuple(self):
        self.assertRaises(ValueError, self.game.move, ())

    def test_move_none(self):
        self.assertRaises(ValueError, self.game.move, None)

    def test_move_wrong_range1(self):
        self.assertRaises(Exception, self.game.move, 0)

    def test_move_wrong_range2(self):
        self.assertRaises(Exception, self.game.move, 8)

    def test_move_back1(self):
        self.game.move(1)
        self.assertEqual(self.game.move_back(), self.empty_board)

    def test_move_back2(self):
        self.game.move(1)
        self.game.move(1)

        self.game.move_back()
        self.game.move_back()

        self.assertEqual(self.game.board, self.empty_board)

    def test_check_board_not_finished(self):
        self.assertFalse(self.game.check_board())

    def test_check_board_draw(self):
        self.game.board = [
            [1, 2, 1, 2, 1, 2, 2],
            [1, 2, 1, 2, 1, 2, 1],
            [2, 1, 2, 1, 2, 1, 2],
            [2, 1, 2, 1, 2, 1, 2],
            [1, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1]]
        self.assertTrue(self.game.check_board())

    def test_check_win_horizontal(self):
        self.game.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [2, 2, 2, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0]]
        self.assertTrue(self.game.check_board())

    def test_check_win_vertical(self):
        self.game.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 2, 0, 0],
            [2, 2, 0, 1, 2, 0, 0],
            [1, 1, 0, 1, 2, 0, 0]]
        self.assertTrue(self.game.check_board())

    def test_check_I_slope(self):
        self.game.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0],
            [0, 1, 1, 2, 0, 0, 0],
            [1, 2, 2, 2, 2, 0, 0]]
        self.assertTrue(self.game.check_board())

    def test_check_II_slope(self):
        self.game.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 2, 1, 0, 0, 0, 0],
            [0, 2, 2, 1, 0, 0, 0],
            [1, 2, 1, 2, 1, 0, 0]]
        self.assertTrue(self.game.check_board())

    def test_move_after_game_end(self):
        self.game.board = self.winning_board
        self.game.check_board()
        self.assertRaises(Exception, self.game.move_back)

    def test_move_back_after_game_end(self):
        self.game.board = self.winning_board
        self.game.check_board()
        self.assertRaises(Exception, self.game.move_back)

    def test_check_winner_name(self):
        self.game.board = self.winning_board
        self.game.check_board()
        self.assertEqual(self.game.winner, "Jacek")

    def test_check_looser_name(self):
        self.game.board = self.winning_board
        self.game.check_board()
        self.assertEqual(self.game.looser, "Wojtas")

    def tearDown(self):
        self.game = None
