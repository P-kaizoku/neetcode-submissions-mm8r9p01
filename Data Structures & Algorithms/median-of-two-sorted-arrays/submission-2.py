class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0,0
        m, n = len(nums1), len(nums2)
        res = []

        while i<m and j<n:
            if nums1[i]<nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        
        while i<m:
            res.append(nums1[i])
            i += 1
        
        while j<n:
            res.append(nums2[j])
            j += 1
        
        s = len(res)
        if s%2==1:
            return float(res[s//2])
        else:
            return (res[s//2] + res[(s//2)-1])/2

