__author__ = 'yusizhang'
class Solution(object):
    """
    Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
    For example,
    Given nums = [0, 1, 3] return 2.
    """
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            # This is a while loop. Cannot be done in if statement
            while nums[i] != i and nums[i] < n:
                tmp  = nums[i]
                nums[i] = nums[tmp]
                nums[tmp] = tmp
        for i in range(n):
            if nums[i] != i:
                return i
        return n
if __name__ == '__main__':
    print Solution().missingNumber([2,0])