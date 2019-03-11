class ConnectFourBoard:  # X is 0 and O is 1#
    map = None
    turn = None
    parent = None
    move = None

    def __init__(self, lst, board = None):
        if board is None:
            self.parent = None
            self.map = {}
            for x in range(0, 42):
                map[x] = lst[42-x]
            self.turn = self.get_turn(lst)
        else:
            self.map = {}
            self.board = board
            if board.turn is 0:
                self.turn = 1
            else:
                self.turn = 0

    def get_turn(self, lst):
        x = 0
        o = 0
        for i in lst:
            if i is 0:
                x += 1
            elif i is 1:
                o += 1
        if x > o:
            return 1
        else:
            return 0

    def get_Utility(self):
        util = 0
        row = check_row()
        col = check_col()
        diag = check_diag()
        antidiag = check_antidiag()
        if row[0] or col[0] or diag[0] or antidiag[0]:
            util = 1
        elif row[1] or col[1] or diag[1] or antidiag[1]:
            util = -1
        return util

    def check_row(self):

    def check_col(self):

    def check_diag(self):

    def check_antidiag(self):

    def min_value(self):

    def max_value(self):

    def minimax_decision(self):

    def print_move(self):

    def next_states(self):

    def terminal_test(self):