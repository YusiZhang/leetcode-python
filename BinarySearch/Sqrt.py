class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start, end = 1, x
        while start + 1 < end:
            mid = start + (end - start) / 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid
            else:
                end = mid
        if end * end <= x:
            return end
        return start

"""binary search template
def binarySearch(self, nums, target):
        '''
        :param nums:
        :param target:
        :return: the index of target in the nums
        '''
        if len(nums) == 0:
            return None
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return None
"""