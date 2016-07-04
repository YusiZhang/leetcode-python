class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 3
        bitCount = [0 for _ in range(32)]
        for j in range(len(nums)):
            n = nums[j]
            for i in range(32):
                hasBit = (n & (1 << i)) != 0
                if hasBit:
                    bitCount[i] = (bitCount[i] + 1) % k
        result = 0
        for i in range(32):
            if bitCount[i] > 0:
                result = result | (1 << i)

        # return result
        return self.convert(result)
        
    def convert(self,x):
        if x >= 2**31:
            x -= 2**32
        return x