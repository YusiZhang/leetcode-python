class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        M(k) = money at the kth house
        P(0) = 0
        P(1) = M(1)
        P(k) = max(P(k−2) + M(k), P(k−1))
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [None]*len(nums)
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in xrange(2, len(nums)):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        
        return dp[len(nums)-1]
        
"""
public int rob(int[] nums) {  
    if(nums.length==0) return 0;
    if(nums.length==1) return nums[0];

    //Initialize an arrays to store the money
    int[] mark = new int[nums.length];

    //We can infer the formula from problem:mark[i]=max(num[i]+mark[i-2],mark[i-1])
    //so initialize two nums at first.
    mark[0] = nums[0];
    mark[1] = Math.max(nums[0], nums[1]);

    //Using Dynamic Programming to mark the max money in loop.
    for(int i=2;i<nums.length;i++){
        mark[i] = Math.max(nums[i]+mark[i-2], mark[i-1]);
    }
    return mark[nums.length-1];
}
"""
        