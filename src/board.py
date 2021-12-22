class Board:
    def __init__(self, rows=6, columns=7):
        self.separator = 0
        self.board = [[self.separator for i in range(columns)] for j in range(rows)]
        self.rows = 6
        self.columns = 7

    def print_board(self):
        for col in self.board:
            print(col)
        print("\n")


    '''def check_board(self, player1_color, player2_color):
        # Check horizontal
        for c in range(4):
            for r in range(6):
                if self.board[r][c] == self.board[r][c + 1] == self.board[r][c + 2] == self.board[r][c + 3] \
                        and self.board[r][c] in [player1_color, player2_color]:
                    if self.board[r][c] == player1_color:
                        self.winner = self.player1_name
                        self.looser = self.player2_name
                    else:
                        self.winner = self.player2_name
                        self.looser = self.player2_name
                    self.game_end = True
                    self.save_result()
                    return True

        # Check vertical
        for c in range(7):
            for r in range(3):
                if self.board[r][c] == self.board[r + 1][c] == self.board[r + 2][c] == self.board[r + 3][c] \
                        and self.board[r][c] in [self.player1_color, self.player2_color]:
                    if self.board[r][c] == self.player1_color:
                        self.winner = self.player1_name
                        self.looser = self.player2_name
                    else:
                        self.winner = self.player2_name
                        self.looser = self.player1_name
                    self.game_end = True
                    self.save_result()
                    return True

        # Check I slope
        for c in range(4):
            for r in range(3):
                if self.board[r][c] == self.board[r + 1][c + 1] == self.board[r + 2][c + 2] == \
                        self.board[r + 3][c + 3] and self.board[r][c] in [self.player1_color, self.player2_color]:
                    if self.board[r][c] == self.player1_color:
                        self.winner = self.player1_name
                        self.looser = self.player2_name
                    else:
                        self.winner = self.player2_name
                        self.looser = self.player1_name
                    self.game_end = True
                    self.save_result()
                    return True

        # Check II slope
        for c in range(4):
            for r in range(3, 6):
                if self.board[r][c] == self.board[r - 1][c + 1] == self.board[r - 2][c + 2] == \
                        self.board[r - 3][c + 3] and self.board[r][c] in [self.player1_color, self.player2_color]:
                    if self.board[r][c] == self.player1_color:
                        self.winner = self.player1_name
                        self.looser = self.player2_name
                    else:
                        self.winner = self.player2_name
                        self.looser = self.player1_name
                    self.game_end = True
                    self.save_result()
                    return True

        # Draw
        if self.separator not in (
                self.board[0] or self.board[1] or self.board[2] or self.board[3] or self.board[4] or self.board[5]):
            self.game_end = True
            self.save_result()
            return True

        return False'''