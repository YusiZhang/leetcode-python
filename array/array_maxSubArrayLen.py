__author__ = 'yusizhang'
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # No need to allocate spaces for sums_dp
        current_sum = 0
        max_length = 0
        dict = {0:-1}
        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum not in dict:
                dict[current_sum] = i
            if current_sum - k in dict:
                max_length = max(max_length, i - dict[current_sum - k])
        return max_length
        # sum range dp solution
        # sum[i] means sum from 0 to i inclusively.
        # ai...aj sum will be sum[j] - sum[i-1]
        # if i = 0, a0...ai will be sum[j]. No need to minus sum[0-1]


if __name__ == '__main__':
    print Solution().maxSubArrayLen([-2,-1,2,1], 1)
    print Solution().maxSubArrayLen([1,-1,5,-2,3], 3)