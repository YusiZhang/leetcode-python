class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        a = 0
        b = 0
        for num in nums:
            xor ^= num
        mask = xor & -xor # bit hack, isolate the right most 1 bit
        for num in nums:
            if num&mask:
                a ^= num
            else:
                b ^= num
        return [a, b]
        
"""

An easier method to get the negation of a number in two's complement is as follows:

Example 1	Example 2
1. Starting from the right, find the first "1"	00101001	00101100
2. Invert all of the bits to the left of that one	11010111	11010100
Method two:

Invert all the bits through the number
Add one
Example: for +1, which is 00000001 in binary:

~00000001 → 11111110
11111110 + 1 → 11111111 (−1 in two's complement)



"""
        