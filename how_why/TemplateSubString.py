import sys


class SubStringTemplate:
    def minWindow(self, s, t):
        if t == "" or s == "":
            return ""
        d, dt = {}, dict.fromkeys(t, 0)
        for c in t:
            d[c] = d.get(c, 0) + 1
        start, end, count = 0, 0, 0
        ans = ""
        while end < len(s):
            if s[end] in dt:
                if dt[s[end]] < d[s[end]]:
                    count += 1
                dt[s[end]] += 1
            if count == len(t):
                while start < end:
                    if s[start] in dt:
                        if dt[s[start]] == d[s[start]]:
                            break
                        dt[s[start]] -= 1
                    start += 1
                if ans == "" or end - start < len(ans):
                    ans = s[start:end+1]
                dt[s[start]] -= 1
                start += 1
                count -= 1
            end += 1
            # ord("x")
        return ans






    # def minWindow(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: str
    #     """
    #     m = {}
    #     for c in t:
    #         m[c] += 1
    #     # counter represents the number of chars of t to be found in s.
    #     start = end = 0
    #     counter = len(t)
    #     minStart = 0
    #     minLen = -1 - sys.maxint
    #     size = len(s)
    #
    #     # Move end to find a valid window
    #     while end < size:
    #         # if char in s exists in t, decrease counter
    #         if m[s[end]] > 0:
    #             counter -= 1
    #         # Decrease m[s[end]]. If char doesn't exist in t, m[s[end]] will be negative
    #         m[s[end]] -= 1
    #         end += 1
    #         # When we found a valid window, move start to find smaller window.
    #         while counter == 0:
    #             if end - start < minLen:
    #                 minStart = start
    #                 minLen = end - start
    #             m[s[start]] += 1
    #             # When char exists in t, increase counter
    #             if m[s[start]] > 0:
    #                 counter += 1
    #             start += 1
    #     if minLen != -1 - sys.maxint:
    #         return s[minStart:minLen]
    #     return ""