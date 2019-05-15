import connectfour
import sys


class ConnectFour:

    def solver(self, filename):
        try:
            file = open(filename, "r")
            lst = []
            count = 0
            for line in file:
                if len(line) != 8:
                    raise ValueError()
                count += 1
                for x in range(0, len(line)):
                    if line[len(line)-x-2] == ".":
                        lst.append(-1)
                    elif line[len(line)-x-2] == 'X':
                        lst.append(0)
                    elif line[len(line)-x-2] == 'O':
                        lst.append(1)
            print(len(lst))
            board = connectfour.ConnectFourBoard(lst)
            ret = board.minimax_decision()
            board.print_move(ret)
            if count != 6:
                raise ValueError()
            file.close()
        except IOError:
            file.close()
            print("Cannot open the file.")
        except ValueError:
            file.close()
            print("Incorrect board dimensions.")

    if __name__ == "__main__":
        if len(sys.argv)-1 != 1:
            print("Need 1 argument.")
        else:
            file = sys.argv[1]
            run = connectfour.ConnectFour()
            run.solver(file)


class ConnectFourBoard:  # X is 0 and O is 1#
    map = None
    turn = None
    parent = None
    move = None

    def __init__(self, lst, board=None):
        if board is None:
            self.parent = None
            self.map = {}
            for x in range(0, 42):
                self.map[x] = lst[41-x]
            self.turn = self.get_turn(lst)
        else:
            self.map = {}
            self.board = board
            if board.turn is 0:
                self.turn = 1
            else:
                self.turn = 0

    def get_turn(self, lst: [int]) -> int:
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

    def get_utility(self):
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
            for x in range(1, 4):
                if val != self.map.get(i+x):
                    break
                if x == 3:
                    ret[val] = True
                    return ret
            if i % 7 == 3:
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

    def check_tie(self, lst):
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
        if self.terminal_test():
            return self.get_utility()
        val = 10000
        lst = self.next_states()
        if not lst:
            for x in lst:
                comp = x.max_value()
                if val > comp:
                    val = comp
        return val

    def max_value(self):
        if self.terminal_test():
            return self.get_utility()
        val = -10000
        lst = self.next_states()
        if not lst:
            for x in lst:
                comp = x.min_value()
                if val < comp:
                    val = comp
        return val

    def minimax_decision(self):
        val = 0
        if self.turn:
            val = self.min_value()
        else:
            val = self.max_value()
        if val != 1 and val != -1:
            val = 0
        return val

    def print_move(self, max_val):
        lst = self.next_states()
        for x in lst:
            com: int = 0
            if self.turn:
                com = x.max_value()
            else:
                com = x.min_value()
            if com != 1 and com != -1:
                com = 0
            if com == max_val:
                if self.turn:
                    print("Utility: " + max_val + " O" + x.move)
                else:
                    print("Utility: " + max_val + " X" + x.move)
            break

    def next_states(self):
        ret = []
        if not self.terminal_test():
            for x in range(0, 7):
                for y in range(0, 6):
                    if self.map.get(x+7*y) == -1:
                        to_add = ConnectFourBoard(self)
                        to_add.move = x
                        to_add.map[x+7*y] = to_add.parent.turn
                        ret.append(to_add)
                        break
        return ret

    def terminal_test(self):
        row = self.check_row()
        col = self.check_col()
        diag = self.check_diag()
        antidiag = self.check_antidiag()
        if row.get(0) or col.get(0) or diag.get(0) or antidiag.get(0):
            return True
        elif row.get(1) or col.get(1) or diag.get(1) or antidiag.get(1):
            return True
        return False
