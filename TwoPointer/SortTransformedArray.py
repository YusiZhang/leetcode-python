"""
the problem seems to have many cases a>0, a=0,a<0, (when a=0, b>0, b<0). However, they can be combined into just 2 cases: a>0 or a<0

1.a>0, two ends in original array are bigger than center if you learned middle school math before.

2.a<0, center is bigger than two ends.

so use two pointers i, j and do a merge-sort like process. depending on sign of a, you may want to start from the beginning or end of the transformed array. For a==0 case, it does not matter what b's sign is. The function is monotonically increasing or decreasing. you can start with either beginning or end.
"""
class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        i = 0
        j = n - 1
        index = n-1 if a >=0 else 0
        while i <= j:
            if a >= 0:
                if self.quand(nums[i], a, b, c) >= self.quand(nums[j],a,b,c):
                    result[index] = self.quand(nums[i], a,b,c)
                    i += 1
                else:
                    result[index] = self.quand(nums[j], a,b,c)
                    j -= 1
                index -= 1
            else:
                if self.quand(nums[i], a, b, c) <= self.quand(nums[j],a,b,c):
                    result[index] = self.quand(nums[i], a,b,c)
                    i += 1
                else:
                    result[index] = self.quand(nums[j], a,b,c)
                    j -= 1
                index += 1
        return result
                
    def quand(self, x, a, b, c):
        return a*x**2 + b*x + c