__author__ = 'yusizhang'

class BinarySearch(object):
    def binarySearch(self, nums, target):
        '''
        :param nums:
        :param target:
        :return: the index of target in the nums
        '''
        if len(nums) == 0:
            return None
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return None

if __name__ == '__main__':
    print BinarySearch().binarySearch([1,2,3,4,5,6], 5)
    print BinarySearch().binarySearch([1,2,3,4,5,6,7], 5)