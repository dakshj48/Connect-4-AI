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
        if abs(x-o) > 1:
            return -1  # "Invalid board!"#
        if x > o:
            return 1
        else:
            return 0

    def get_Utility(self):
        util = 0
        row = self.check_row()
        col = self.check_col()
        diag = self.check_diag()
        antidiag = self.check_antidiag()
        if row[0] or col[0] or diag[0] or antidiag[0]:
            util = 1
        elif row[1] or col[1] or diag[1] or antidiag[1]:
            util = -1
        return util

    def check_row(self):
        ret = {0: False, 1: False}
        i = 0
        while i < 39:
            val = self.map.get(i)
            for x in range(1,4):
                if val != self.map.get(i+x):
                    break
                if x == 3:
                    ret[val] = True
                    return ret
            if i%7 == 3
                i += 3
            i += 1
        return ret

    def check_col(self):
        ret = {0: False, 1: False}
        i = 0
        while i < 21:
            val = self.map.get(i)
            for x in range(1, 4):
                if val != self.map.get(i+x*7):
                    break
                if x == 3:
                    ret[val] = True
                    return ret
            i += 1
        return ret

    def check_diag(self):
        ret = {0: False, 1: False}
        i = 0
        while i < 18:
            val = self.map.get(i)
            for x in range(1, 4):
                if val != self.map.get(i+x*8):
                    break
                if x == 3:
                    ret[val] = True
                    return ret
            i += 1
            if i == 4:
                i = 7
            elif i == 11:
                i = 14
        return ret

    def check_antidiag(self):
        ret = {0: False, 1: False}
        i = 3
        while i < 21:
            val = self.map.get(i)
            for x in range(1, 4):
                if val != self.map.get(i+x*6):
                    break
                if x == 3:
                    ret[val] = True
            i += 1
            if i == 7:
                i = 10
            elif i == 14:
                i = 17
        return ret

    def check_tie(self):
        for x in lst:
            if x == -1:
                return False
        return True

    def valid_board(self):
        i = 0
        while i < 21:
            val = self.map.get(i)
            if val == -1:
                for x in range(1, 4):
                    if val != self.map.get(i + x * 7):
                        return False
            i += 1
        return True

    def min_value(self):

    def max_value(self):

    def minimax_decision(self):

    def print_move(self):

    def next_states(self):

    def terminal_test(self):