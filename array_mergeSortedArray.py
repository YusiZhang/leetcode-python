__author__ = 'yusizhang'
class Solution(object):
    """
    Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
    Note:
    You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
    The number of elements initialized in nums1 and nums2 are m and n respectively.
    """
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        pointer1 = m - 1
        pointer2 = n - 1
        tailPointer = m + n - 1
        while pointer1 >= 0 and pointer2 >= 0:
            if nums1[pointer1] > nums2[pointer2]:
                nums1[tailPointer] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[tailPointer] = nums2[pointer2]
                pointer2 -= 1
            tailPointer -= 1
        while pointer1 >= 0:
            nums1[tailPointer] = nums1[pointer1]
            tailPointer -= 1
            pointer1 -= 1
        while pointer2 >= 0:
            nums1[tailPointer] = nums2[pointer2]
            tailPointer -= 1
            pointer2 -= 1
if __name__ == '__main__':
    nums1 = [1,3,5,7,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    nums2 = [2,4,6,8]
    Solution().merge(nums1, 5, nums2, 4)
    print nums1