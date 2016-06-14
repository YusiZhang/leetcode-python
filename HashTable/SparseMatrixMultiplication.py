# only table B to detecting non-zero elements.
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if A is None or B is None: return None
        m, n, l = len(A), len(A[0]), len(B[0])
        if len(B) != n:
        	raise Exception("A's column number must be equal to B's row number")
        C = [[0 for _ in xrange(l)] for _ in xrange(m)]
        tableB = {}
        for k, row in enumerate(B):
        	tableB[k] = {}
        	for j, eleB in enumerate(row):
        		if eleB:
        			tableB[k][j] = eleB
        for i, row in enumerate(A):
        	for k, eleA in enumerate(row):
        		if eleA:
        			for j, eleB in tableB[k].iteritems():
        				C[i][j] += eleA * eleB
        return C

# Python solution without tables
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if A is None or B is None: return None
        m, n, l = len(A), len(A[0]), len(B[0])
        if len(B) != n:
            raise Exception("A's column number must be equal to B's row number.")
        C = [[0 for _ in range(l)] for _ in range(m)]
        for i, row in enumerate(A):
            for k, eleA in enumerate(row):
                if eleA:
                    for j, eleB in enumerate(B[k]):
                        if eleB: C[i][j] += eleA * eleB
        return C