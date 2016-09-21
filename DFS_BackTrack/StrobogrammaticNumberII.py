class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        
        if int(low) > int(high):
            return 0
        # real_high = max(int(low), int(high))
        # real_low = min(int(low), int(high))
        nums = []
        for i in range(len(low), len(high)+1):
            nums.extend(self.findStrobogrammatic(i))
        return len([n for n in nums if int(low) <= int(n) <= int(high)])
        # return nums

    def findStrobogrammatic(self, n):
        even = ["11","69","88","96", "00"]
        odd  = ["0", "1", "8"]

        if n == 1:
            return odd
        if n == 2:
            return even[:-1]
        if n % 2: #odd ie 3
            pre, mid = self.findStrobogrammatic(n-1), odd
        else: #even
            pre, mid = self.findStrobogrammatic(n-2), even
        premid = (n-1)/2
        return [p[:premid] + c + p[premid:] for p in pre for c in mid]

if __name__ == '__main__':
    solution = Solution()
    nums = solution.findStrobogrammatic(3)
    print nums
    print solution.strobogrammaticInRange("50", "100")