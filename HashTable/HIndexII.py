"""
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

Hint:

Expected runtime complexity is in O(log n) and the input is sorted.
"""
"""
Just binary search, each time check citations[mid] 
case 1: citations[mid] == len-mid, 
then it means there are citations[mid] papers that have at least citations[mid] citations. 

case 2: citations[mid] > len-mid, 
then it means there are citations[mid] papers that have moret than citations[mid] citations, 
so we should continue searching in the left half case 3: citations[mid] < len-mid, 
we should continue searching in the right side After iteration, 
it is guaranteed that right+1 is the one we need to find (i.e. len-(right+1) papars have at least len-(righ+1) citations)
"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        left, right, length = 0, len(citations) - 1, len(citations)
        while left < right + 1:
        	mid = left + (right - left)/2
        	if citations[mid] >= length - mid:
        		right = mid - 1
        	else:
        		left = mid + 1

        return length - left 