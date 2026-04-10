class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = 1000
        l,r = 0, len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                ans = min(ans, nums[l])
                break
            
            mid = l + (r-l)//2
            ans = min(ans, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        return ans