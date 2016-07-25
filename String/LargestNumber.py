"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        num = [str(x) for x in nums]
        num.sort(cmp=lambda x, y: cmp(y+x, x+y)) ### very cleaver way to compare 30 and 3: 330 > 303. 
        #So the number should be 330...to make it bigger
        return ''.join(num).lstrip('0') or '0'