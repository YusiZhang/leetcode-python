# coding=utf-8
__author__ = 'yusizhang'


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # http://fisherlei.blogspot.com/2013/01/leetcode-trapping-rain-water.html
        if len(height) < 2:
            return 0
        maxHeightLeft = [0] * len(height)
        maxHeightRight = [0] * len(height)

        maxHeightLeft[0] = 0
        currentMax = height[0]
        # 计算到第i个坐标时左边最高的高度maxHeightLeft[i]
        for i in range(1, len(height)):
            maxHeightLeft[i] = currentMax
            currentMax = max(maxHeightLeft[i], height[i])

        currentMax = height[len(height) - 1]
        maxHeightRight[len(height) - 1] = 0
        # 计算到第i个坐标时右边最高的高度maxHeightReft[i]
        for i in range(len(height) - 2, -1, -1):
            maxHeightRight[i] = currentMax
            currentMax = max(maxHeightRight[i], height[i])

        sum = 0
        # 第i坐标处可蓄水的值等于此处左右两侧最高值中的较小值，与当前坐标高度的差
        for i in range(len(height) - 1, -1, -1):
            sum += min(maxHeightRight[i], maxHeightLeft[i]) - height[i] if min(maxHeightRight[i], maxHeightLeft[i]) > \
                                                                           height[i] else 0
        return sum


if __name__ == '__main__':
    height = [2, 0, 2]
    print Solution().trap(height)
    height = [0, 2, 0]
    print Solution().trap(height)
