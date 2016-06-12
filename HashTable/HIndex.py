class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # sort the citations descending order --> this is wrong since it just returns the sorted array, but not sort the original array!
        # sorted(citations, reverse=True)
        citations.sort(reverse=True)
        # finding h-index by linear search
        i = 0
        while i < len(citations) and citations[i] > i:
        	i += 1
        return i # after the while loop, i = i' + 1