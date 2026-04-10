class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i,j = 0,0
        m,n = len(nums1), len(nums2)
        ans = []
        while i<m and j<n:

            if nums1[i]>nums2[j]:
                ans.append(nums2[j])
                j += 1
            else:
                ans.append(nums1[i])
                i += 1
        
        while i<m:
            ans.append(nums1[i])
            i+=1
        
        while j<n:
            ans.append(nums2[j])
            j += 1
        
        s = len(ans)
        if s%2==0:
            return (ans[s//2]+ans[(s//2)-1])/2
        return ans[(s//2)]