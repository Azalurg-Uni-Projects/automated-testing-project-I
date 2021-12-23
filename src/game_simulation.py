import random

from src.game import Game

rows = 4
columns = 7
player1 = "Bob"
player2 = "Ivona"

game = Game(player1, player2, rows, columns)

while not game.game_end:
    try:
        move = random.randint(1, columns+1)
        game.move(move)
    except:
        pass

print("=====", game.winner, "=====")
game.print_board()
