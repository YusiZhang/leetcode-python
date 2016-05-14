# coding=utf-8
__author__ = 'yusizhang'
"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        partition = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                # 从后向前找到第一个升序对，并让partition等于升序对中较小的
                # 如145326中45是升序对，则partition等于4
                partition = i
                # don't forget breaking out here
                break

        if partition == -1:
            # 没找到升序对 e.g. 54321 --> 12345
            nums.reverse()
        else:
            for i in range(len(nums)-1, partition, -1):
                if nums[i] > nums[partition]:
                    # 交换partition和升序对后面比partition更大的数 如14532 -> 15432
                    nums[i], nums[partition] = nums[partition], nums[i]
                    break
                    # 将partition后面的数字逆向排序。由于找到的partition是从后向前的第一个升序对，所以可以放心partition后面一定都是降序的
                    # 所以逆向排序后可以得到一个新的刚好大于之前permutation的next permutation
                    # 比如此时14532已经变为15432，则再将5（此时partition已经是5了）后面的432逆序排列得到234.则最终的数字变为15234
            nums[partition+1:] = nums[partition+1:][::-1]
        # return nums
