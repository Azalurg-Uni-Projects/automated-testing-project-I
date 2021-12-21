import unittest
from src.gra import Game

class Game_test(unittest.TestCase):

    def setUp(self):
        game = Game("Jacek", "Wojtas")
        self.game = game
    
    def test_check_init_val_player1(self):
        self.assertEqual(self.game.player1_name, "Jacek")

    def test_check_init_val_player2(self):
        self.assertEqual(self.game.player2_name, "Wojtas")

    def tearDown(self):
        self.game = None