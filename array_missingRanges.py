__author__ = 'yusizhang'
class Solution(object):
    """
    Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.
    For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
    """
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        #Just simply insert lower-1 and upper+1 into the list
        #The missing range should be num[i]+1 ~ num[i+1]-1
        nums.insert(0, lower - 1)
        nums.append(upper + 1)
        ans = []
        i = 0
        while i < len(nums) - 1:
            if nums[i+1] - nums[i] == 1:
                pass
            if nums[i+1] - nums[i] == 2:
                ans.append(str(nums[i] + 1))
            if nums[i+1] - nums[i] > 2:
                ans.append(str(nums[i]+1) + "->" + str(nums[i+1]-1))
            i += 1
        return ans