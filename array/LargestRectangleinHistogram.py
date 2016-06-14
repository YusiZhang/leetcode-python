class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        i = 0
        area = 0

        while i < len(heights):
        	if stack == [] or heights[i] > heights[stack[len(stack)-1]]:
        		stack.append(i)
        		i += 1
        	else:
        		current = stack.pop()
        		width = i if stack == [] else i-stack[len(stack)-1]-1
        		area = max(area, width*heights[current])

        while stack != []:
        	current = stack.pop()
        	width = i if stack == [] else len(heights) - stack[len(stack)-1] -1
        	area = max(area, width*heights[current])

        return area