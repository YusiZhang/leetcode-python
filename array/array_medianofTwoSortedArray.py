class Solution(object):
    # def findMedianSortedArrays(self, nums1, nums2):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: float
    #     """
    #     n = len(nums1) + len(nums2)
    #     if n % 2 == 1:
    #         return self.findKth(nums1, nums2, n/2 + 1)
    #     else:
    #         return (self.findKth(nums1, nums2, n / 2) + self.findKth(nums1, nums2, n / 2 + 1)) / 2.0
        
    # def findKth(self, A, B, k):
    #     if len(A) == 0:
    #         return B[k-1]
    #     if len(B) == 0:
    #         return A[k-1]
    #     if k == 1:
    #         return min(A[0], B[0])
    #     a = A[k/2 - 1] if len(A) >= k / 2 else None
    #     b = B[k/2 - 1] if len(B) >= k / 2 else None
    #     if b is None or (a is not None and a < b):
    #         return self.findKth(A[k/2:], B, k - k/2)
            
    #     return self.findKth(A,B[k/2:], k - k/2)
        
    def findMedianSortedArrays(self, nums1, nums2):
        length = len(nums1) + len(nums2)
        if length == 0:
            return None
        if length % 2 == 1: #odd
            return self.findKth(nums1, 0, nums2, 0, length / 2 + 1)
        else:
            return ( self.findKth(nums1, 0, nums2, 0, length / 2) + self.findKth(nums1, 0, nums2, 0, length / 2 + 1) ) / 2.0
    
    def findKth(self, A, A_start, B, B_start, k):
        if A_start >= len(A):
            return B[B_start + k - 1] # index is 0 base
        if B_start >= len(B):
            return A[A_start + k - 1]
        if k == 1:
            return min(A[A_start], B[B_start])
        A_key = A[A_start + k/2 -1] if A_start + k/2 -1 < len(A) else sys.maxint
        B_key = B[B_start + k/2 -1] if B_start + k/2 -1 < len(B) else sys.maxint
        
        if A_key < B_key:
            return self.findKth(A, A_start + k/2, B, B_start, k - k/2)
        else:
            return self.findKth(A, A_start, B, B_start + k/2, k - k/2)
        

        
        