"""
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples:
"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
"""

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = []
        if not num:
            return res
        self.dfs_backtrack(res, "", num, target, 0, 0, 0)
        return res

    def dfs_backtrack(self, res, path, num, target, pos, eval, multed):
        if pos == len(num):
            if target == eval:
                res.append(str(path))
            return

        for i in range(pos, len(num)):
            if i != pos and num[pos] == '0': break
            cur = int(num[pos:i+1])
            if pos == 0:
                self.dfs_backtrack(res, path+str(cur), num, target, i+1, cur, cur)
            else:
                self.dfs_backtrack(res, path + "+" + str(cur), num, target, i+1, eval + cur, cur)

                self.dfs_backtrack(res, path + "-" + str(cur), num, target, i+1, eval - cur, -cur)

                self.dfs_backtrack(res, path + "*" + str(cur), num, target, i+1, eval - multed + multed*cur, multed*cur)