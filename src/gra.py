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
        self.moves = []
        self.winner = None
        self.looser = None
        self.game_end = False

    def print_board(self):
        for col in self.board:
            print(col)
        print("\n")

    def change_player(self):
        if self.next == self.player1:
            self.next = self.player2
        else:
            self.next = self.player1

    def check_board(self):
        # Check horizontal
        for c in range(4):
            for r in range(6):
                if self.board[r][c] == self.board[r][c + 1] == self.board[r][c + 2] == self.board[r][c + 3] \
                        and self.board[r][c] in [self.player1, self.player2]:
                    if self.board[r][c] == self.player1:
                        self.winner = self.player1_name
                        self.looser = self.player2_name
                    else:
                        self.winner = self.player2_name
                        self.looser = self.player2_name
                    self.game_end = True
                    return True

        # Check vertical
        for c in range(7):
            for r in range(3):
                if self.board[r][c] == self.board[r + 1][c] == self.board[r + 2][c] == self.board[r + 3][c] \
                        and self.board[r][c] in [self.player1, self.player2]:
                    if self.board[r][c] == self.player1:
                        self.winner = self.player1_name
                        self.looser = self.player2_name
                    else:
                        self.winner = self.player2_name
                        self.looser = self.player1_name
                    self.game_end = True
                    return True

        # Check I slope
        for c in range(4):
            for r in range(3):
                if self.board[r][c] == self.board[r + 1][c + 1] == self.board[r + 2][c + 2] == \
                        self.board[r + 3][c + 3] and self.board[r][c] in [self.player1, self.player2]:
                    if self.board[r][c] == self.player1:
                        self.winner = self.player1_name
                        self.looser = self.player2_name
                    else:
                        self.winner = self.player2_name
                        self.looser = self.player1_name
                    self.game_end = True
                    return True

        # Check II slope
        for c in range(4):
            for r in range(3, 6):
                if self.board[r][c] == self.board[r - 1][c + 1] == self.board[r - 2][c + 2] == \
                        self.board[r - 3][c + 3] and self.board[r][c] in [self.player1, self.player2]:
                    if self.board[r][c] == self.player1:
                        self.winner = self.player1_name
                        self.looser = self.player2_name
                    else:
                        self.winner = self.player2_name
                        self.looser = self.player1_name
                    self.game_end = True
                    return True

        # Draw
        if self.separator not in (
                self.board[0] or self.board[1] or self.board[2] or self.board[3] or self.board[4] or self.board[5]):
            self.game_end = True
            return True

        return False

    def move(self, col):
        if self.game_end:
            print("Koniec gry, wygrał: {}".format(self.winner))
            return self.board
        if type(col) is not int:
            print("!!! BŁĘDNE DANE WEJŚCIOWE {} !!!".format(type(col)))
            return self.board
        if col not in range(1, 8):
            print("!!! ZŁY ZAKRES !!!")
            return self.board
        col -= 1
        if self.board[0][col] == self.separator:
            for i in range(5, -1, -1):
                if self.board[i][col] == self.separator:
                    self.board[i][col] = self.next
                    self.moves.append(col)
                    self.check_board()
                    self.change_player()
                    break
        else:
            print("Nie mogę wykonać ruchu, kolumna {} pełna, spróbuj ponownie.".format(col + 1))

        return self.board

    def move_back(self):
        if self.game_end:
            print("Koniec gry, wygrał: {}".format(self.winner))
            return self.board
        if not self.moves:
            print("Nie można cofnąć ruchu")
            return self.board
        else:
            col = self.moves.pop()
            for i in range(5, -1, -1):
                if self.board[i][col] != self.separator:
                    self.board[i][col] = self.separator
                    self.change_player()
                    return self.board
            return self.board
