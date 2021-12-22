class Board:
    def __init__(self, rows=6, columns=7):
        self.separator = 0
        self.board = [[self.separator for i in range(columns)] for j in range(rows)]

    def print_board(self):
        for col in self.board:
            print(col)
        print("\n")
