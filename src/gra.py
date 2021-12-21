# rows = 6 columns = 7

class Game:
    def __init__(self, player1_name="player1", player2_name="player2"):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1 = 1
        self.player2 = 2
        self.separator = 0
        self.board = [[self.separator for i in range(7)] for j in range(6)]
        self.next = self.player1

    def print_board(self):
        for col in self.board:
            print(col)
        print("\n")

    def change_player(self):
        if self.next == self.player1:
            self.next = self.player2
        else:
            self.next = self.player1


gra = Game("Jacek", "Wojtas")
gra.print_board()
