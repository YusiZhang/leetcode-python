class WordSearchII(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        root = self.buildTrie(words)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, root, res)
        return res

    def dfs(self, board, i, j, node, res):
        c = board[i][j]
        if c == "#" or c not in node.children:
            return
        node = node.children[c]
        if node.word is not None:
            res.append(node.word)
            node.word = None

        board[i][j] = "#"
        if i > 0 : self.dfs(board, i-1, j, node, res)
        if j > 0 : self.dfs(board, i, j - 1, node, res)
        if i < len(board) - 1 : self.dfs(board, i+1, j, node, res)
        if j < len(board[0]) - 1 : self.dfs(board, i, j+1, node, res)
        board[i][j] = c

    def buildTrie(self, words):
        root = TrieNode()
        for w in words:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = w
        return root


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.word = None

if __name__ == '__main__':
    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]
    solution = WordSearchII()
    print solution.findWords(board, words)




