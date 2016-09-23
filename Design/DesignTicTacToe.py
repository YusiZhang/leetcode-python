import collections


class TicTacToe(object):

    def __init__(self, n):
        count = collections.Counter()
        def move(row, col, player):
            for i, x in enumerate((row, col, row+col, row-col)):
                count[i, x, player] += 1
                if count[i, x, player] == n:
                    return player
            return 0
        self.move = move




if __name__ == '__main__':
    tictactoe = TicTacToe(3)
    tictactoe.move(0,0,1)
    tictactoe.move(1,0,1)
    tictactoe.move(2,0,1)


        # Your TicTacToe object will be instantiated and called as such:
        # obj = TicTacToe(n)
        # param_1 = obj.move(row,col,player)