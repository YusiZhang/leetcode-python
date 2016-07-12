"""
 Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity. 
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Revisit BS solution!!!
        # Base case
        if len(nums) == 0 or not nums:
            return 0
        # This will be our array to track longest sequence length
        dp = [None] * len(nums)
        max = -1 - sys.maxint
        
        # 
        for i in xrange(len(nums)):
            # Fill each position with value 1 in the array
            dp[i] = 1
            # Mark one pointer at i. For each i, start from j=0.
            for j in xrange(i):
                # It means next number contributes to increasing sequence.
                if nums[j] < nums[i]:
                    # But increase the value only if it results in a larger value of the sequence than T[i]
                    # It is possible that T[i] already has larger value from some previous j'th iteration
                    # Note that the question says the subsequence, not necessarily consecutive subsequence
                    dp[i] = dp[i] if dp[i] > dp[j] + 1 else dp[j] + 1
            if dp[i] > max:
                max = dp[i]
        return max
        
"""
public static int lengthOfLIS2(int[] nums) {
		if(nums.length == 0 || nums == null){
            return 0;
        }
        int []dp = new int[nums.length];
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < nums.length; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    dp[i] = dp[i] > dp[j] + 1 ? dp[i] : dp[j] + 1;
                }
            }
            if (dp[i] > max) {
                max = dp[i];
            }
        }
        return max;
    }
"""
        