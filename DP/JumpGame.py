class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #dp
        if not nums:
            return False
        can = [False for _ in range(len(nums))]
        can[0] = True
        
        for i in range(1, len(nums)):
            for j in range(i):
                if can[j] and j+nums[j] >= i:
                    can[i] = True
                    break
        
        return can[len(nums)-1]