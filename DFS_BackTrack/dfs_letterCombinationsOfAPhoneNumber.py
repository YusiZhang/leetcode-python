# coding=utf-8
__author__ = 'yusizhang'
"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

dict = {'2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']
        }

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 先建立dict包含所有可能
        dict = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
                }
        # 注意，此题并非简单构建出新的candidates然后按照普通combination来处理。
        # 如果 digits是“23”，构建出的candidates数组是[a,b,c,d,e,f]。此时如果后面按照普通combination处理，
        # 则会出现 "ab" "ac"这样的组合
        # 此解法在递归时同时传入count, 其代表组合余下的(除dict[digits[count]]外)combination需要从dict[digits[count+1]]中循环取得。
        if len(digits) == 0 or not digits:
            return []
        
        self.result = []
        
        self.dfs(0, "", digits, dict)
        
        return self.result
    
    def dfs(self, depth, string, digits, dict):
        if depth == len(digits):
            self.result.append(string)
            return
        # dict[digits[depth]]!!!!
        for letter in dict[digits[depth]]:
            # depth + 1 !!!
            self.dfs(depth+1, string+letter, digits, dict)
            
    
    