"""
["eqdf", "qcpr"]。

((‘q’ - 'e') + 26) % 26 = 12, ((‘d’ - 'q') + 26) % 26 = 13, ((‘f’ - 'd') + 26) % 26 = 2

((‘c’ - 'q') + 26) % 26 = 12, ((‘p’ - 'c') + 26) % 26 = 13, ((‘r’ - 'p') + 26) % 26 = 2

所以"eqdf"和"qcpr"是一组shifted strings。
"""
import collections
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d = collections.defaultdict(list)
        for s in strings:
        	shift = tuple([(ord(c) - ord(s[0])) % 26 for c in s])
        	d[shift].append(s)

        return map(sorted, d.values())
