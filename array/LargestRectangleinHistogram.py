class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        stack = []
        area = 0
        
        for i in range(len(heights) + 1):
            curr = -1 if i == len(heights) else heights[i]
            while stack and curr <= heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1 if stack else i
                area = max(area, h*w)
            
            stack.append(i)
        
        return area

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