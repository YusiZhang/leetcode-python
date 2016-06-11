"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
"""
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
        	return 0
        a = [0 for i in range(len(matrix[0]))]
        maxArea = 0
        for i in range(len(matrix)):
        	for j in range(len(matrix[i])):
        		a[j] = a[j] + 1 if matrix[i][j] == '1' else 0

        	maxArea = max(maxArea, self.largestRectangleArea(a))

        return maxArea
    def largestRectangleArea(self, height):
    	stack = []
    	i = area = 0
    	while i < len(height):
    		if stack == [] or height[i] > height[stack[len(stack)-1]]:
    			stack.append(i)
    			i += 1
    		else:
    			# The method pop() removes and returns last object or obj from the list.
    			curr = stack.pop() #pop last element
    			width = i if stack == [] else i - stack[len(stack)-1] - 1
    			area = max(area, width*height[curr])
    	
    	while stack != []:
    		curr = stack.pop()
    		width = i if stack ==[] else len(height)-stack[len(stack)-1]-1
    		area = max(area, width*height[curr])
    	return area

