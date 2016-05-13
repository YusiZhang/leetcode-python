__author__ = 'yusizhang'
"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result = ""
        k -= 1
        factor = 1
        for i in range(1,n):
            factor *= i

        nums = [1,2,3,4,5,6,7,8,9]
        for i in reversed(range(n)):
            current_digit_index = k / factor
            result += str(nums[current_digit_index])
            # this will remove the actual value from the nums array, not the index
            nums.remove(nums[current_digit_index])

            if i != 0:
                k %= factor
                factor /= i
        return result
