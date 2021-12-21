import unittest
from src.gra import Game

class Game_test(unittest.TestCase):

    def setUP(self):
        game = Game("Jacek", "Wojtas")
        self.temp = game

    def tearDown(self):
        self.temp = None