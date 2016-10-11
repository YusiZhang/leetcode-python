"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.
"""
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #dp
        if not nums:
            return -1
        # state
        steps = [sys.maxint for _ in range(len(nums))]
        # init
        steps[0] = 0
        # func
        for i in range(1, len(nums)):
            for j in range(i):
                if steps[j] != sys.maxint and j + nums[j] >= i:
                    steps[i] = min(steps[i], steps[j]+1)
        
        # answer
        return steps[len(nums)-1]