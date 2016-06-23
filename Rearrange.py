class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        result = [""] * len(str)
        m = {}
        for s in str:
            m[s] = m.get(s, 0) + 1
        m_array = list(m.items())
        sorted_m_array = sorted(m_array, key = lambda t: t[1], reverse=True)

        start = 0
        for item in sorted_m_array:
            count = item[1]
            char = item[0]
            cur = start
            while count > 0:
                if cur >= len(str) or result[cur] != "": #either out of boundary or slot is taken means fails
                    return ""
                result[cur] = char
                count -= 1
                cur += k
            # start += 1
            for i in xrange(len(result)):
                if result[i] == "":
                    start = i
                    break


        return "".join(result)

if __name__ == '__main__':
    print Solution().rearrangeString("aabbcc", 3)
    # print Solution().rearrangeString("aa", 0)