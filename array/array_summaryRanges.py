__author__ = 'yusizhang'
class Solution(object):
    """
    Given a sorted integer array without duplicates, return the summary of its ranges.
    For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
    """
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        #sp: start pointer
        #cp: current pointer
        sp, cp = 0,0
        while cp < len(nums):
            while (cp + 1 < len(nums)) and (nums[cp+1] == nums[cp] + 1):
                cp += 1
            if sp != cp:
                ans.append(str(nums[sp]) + "->" + str(nums[cp]))
            else:
                ans.append(str(nums[cp]))
            cp += 1
            sp = cp
        return ans
