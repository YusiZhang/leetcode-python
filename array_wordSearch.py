__author__ = 'yusizhang'
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        n = len(board)
        m = len(board[0])
        visited = [[False for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if self.findWord(board, visited, i, j, word, 0):
                    return True
        return False

    def findWord(self, board, visited, row, col, word, index):
        if index == len(word):
            return True
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or visited[row][col] or board[row][col] != word[index]:
            return False
        visited[row][col] = True
        if self.findWord(board, visited, row-1, col, word, index+1): return True
        if self.findWord(board, visited, row+1, col, word, index+1): return True
        if self.findWord(board, visited, row, col-1, word, index+1): return True
        if self.findWord(board, visited, row, col+1, word, index+1): return True
        visited[row][col] = False
        return False

if __name__ == '__main__':
    print Solution().exist(["ABCE","SFCS","ADEE"], "ABCCED")