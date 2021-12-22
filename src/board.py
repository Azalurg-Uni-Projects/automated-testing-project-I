class Board:
    def __init__(self, rows=6, columns=7):
        if type(rows) is not int:
            raise ValueError
        elif type(columns) is not int:
            raise ValueError
        elif rows < 4:
            raise Exception("Rows too small")
        elif columns < 4:
            raise Exception("Columns too small")
        else:
            self.separator = 0
            self.board = [[self.separator for i in range(columns)] for j in range(rows)]
            self.rows = rows
            self.columns = columns

    def print_board(self):
        for col in self.board:
            print(col)
        print("\n")

    def check_board(self, player1_color, player2_color):
        row = self.rows
        col = self.columns

        conditions = ((col-3, row, 0, 1, 0, 2, 0, 3),       # horizontal
                      (col, row-3, 1, 0, 2, 0, 3, 0),       # vertical
                      (col-3, row-3, 1, 1, 2, 2, 3, 3),     # vertical I
                      (col-3, row, -1, 1, -2, 2, -3, 3))    # vertical II

        for x in conditions:
            for c in range(x[0]):
                for r in range(x[1]):
                    if self.board[r][c] == self.board[r + x[2]][c + x[3]] == self.board[r + x[4]][c + x[5]] == self.board[r + x[6]][c + x[7]] \
                            and self.board[r][c] in [player1_color, player2_color]:
                        return [True, self.board[r][c]]

        # Draw
        if self.separator not in (
                self.board[0] or self.board[1] or self.board[2] or self.board[3] or self.board[4] or self.board[5]):
            return [True, None]

        return [False, None]
