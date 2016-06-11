"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

"""

"""
https://leetcode.com/problems/minimum-window-substring/
解题思路：
1. 定义两个hashtable, d:有哪些目标字母,每个字母应出现几次 ，dt: 每个目标字母当前出现了多少次
2. start, end, count分别代表当前窗口初始指针，结尾指针和目标字母出现次数
3. 遍历source string，如果count的值和len(target_string)一样时，说明此时的窗口下至少存在一个满足要求的substring
4. 但此substring中，每个目标字母出现的次数可能多余所需出现次数。如source_string=aaabcd, 而target为“abc"。则当前substring可能为"aabc".需要想办法把第一个a去掉。
5. 在去掉第一个a后，求出当前substring的长度，并更新最短substring，如果当前substring比已知最短还短时
代码如下：
"""
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if t == "" or s == "":
            return ""
        # d:有哪些目标字母,每个字母应出现几次 ，dt: 每个目标字母当前出现了多少次   
        d, dt = {}, dict.fromkeys(t, 0)
        for c in t:
            d[c] = d.get(c, 0) + 1
        start, end, count = 0, 0, 0
        ans = ""
        while end < len(s):
            if s[end] in dt:
                if dt[s[end]] < d[s[end]]: # 此时目标字母出现次数还不够
                    count += 1
                dt[s[end]] += 1
            if count == len(t):
                while start < end:
                    if s[start] in dt:
                        if dt[s[start]] == d[s[start]]: #到了满足合法substring的最低条件，不必要的重复出现的字母已被删去。
                            break
                        dt[s[start]] -= 1
                    start += 1
                if ans == "" or end - start < len(ans):
                    ans = s[start:end+1]
                dt[s[start]] -= 1
                start += 1
                count -= 1
            end += 1
        return ans