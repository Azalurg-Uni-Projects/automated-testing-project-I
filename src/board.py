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
        pass
