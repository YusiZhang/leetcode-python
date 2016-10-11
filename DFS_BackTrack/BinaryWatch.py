
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        nums1 = [8,4,2,1]
        nums2 = [32,16,8,4,2,1]
        for i in range(num+1):
            list1 = self.generateDigit(nums1, i)
            list2 = self.generateDigit(nums2, num - i)
            for num1 in list1:
                if num1 >= 12: continue
                for num2 in list2:
                    if num2 >= 60: continue
                    res.append(str(num1) + ":" + (str(num2) if num2 >= 10 else (str(0) + str(num2))))

        return res

    def generateDigit(self, nums, count):
        res = []
        self.generateDigitHelper(nums, count, 0, 0, res)
        return res

    def generateDigitHelper(self, nums, count, pos, sum, res):
        if count == 0:
            res.append(sum)
            return
        for i in range(pos, len(nums)):
            self.generateDigitHelper(nums, count-1, i+1, sum+nums[i], res)

if __name__ == '__main__':
    solution = Solution()
    print solution.readBinaryWatch(1)


