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

    def move(self, row):
        if type(row) is not int:
            print("!!! BŁĘDNE DANE WEJŚCIOWE {} !!!".format(type(row)))
            return self.board
        if row not in range(1, 7):
            print("!!! ZŁY ZAKRES !!!")
            return self.board
        row -= 1
        if self.board[0][row] == self.separator:
            for i in range(5, -1, -1):
                if self.board[i][row] == self.separator:
                    self.board[i][row] = self.next
                    self.change_player()
                    break
        else:
            print("Nie mogę wykonać ruchu, kolumna {} pełna, spróbuj ponownie.".format(row + 1))

        return self.board
