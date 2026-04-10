class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
        
        n,m = len(nums1), len(nums2)
        lo, hi = 0, n
        half = (n+m)//2

        while lo <= hi:
            i = (lo+hi)//2
            j = half - i

            maxA = nums1[i-1] if i>0 else float('-inf')
            maxB = nums2[j-1] if j>0 else float('-inf')
            minA = nums1[i] if i<n else float('inf')
            minB = nums2[j] if j<m else float('inf')

            if maxA <= minB and maxB <= minA:
                if (n+m)%2==1:
                    return float(min(minA, minB))    
                return (max(maxA, maxB) + min(minA, minB))/2
            elif maxB > minA:
                lo = i + 1
            else:
                hi = i - 1