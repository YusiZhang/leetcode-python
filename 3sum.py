__author__ = 'yusizhang'

import itertools

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        final_result = []
        for i in range(len(nums)):
            value = nums[i]
            hasTwoSum, result = self.twoSum(nums, -1 * value)
            if hasTwoSum:
                if i < result[0]:
                    result.insert(0, i)
                elif i > result[1]:
                    result.append(i)
                else:
                    result.insert(1, i)
                final_result.append(result)
        final_result.sort()
        # final_result = list(final_result for final_result, _ in itertools.groupby(final_result))
        final_result = list(key for key, value in itertools.groupby(final_result))
        return final_result

    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            value = nums[i]
            # if target - value in dict:
            #     if i < nums[target - value]:
            #         return True, [i, nums[target - value]]
            #     else:
            #         return True, [nums[target - value], i]
            if target - value in dict:
                # must have ( to make them tuples
                return (True, [i, nums[target - value]]) if i < nums[target - value] else (True, [nums[target - value], i])
            dict[value] = i
        return False, []


if __name__ == '__main__':
    print Solution().threeSum([-1, 0, 1, 2, -1, -4])
    my_list = [1,2,3,4,9]
    my_list.reverse()
    print my_list
