class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        leftProd = [1]*n
        

        for i in range(1, n):
            leftProd[i] = nums[i-1]*leftProd[i-1]
        r = 1
        for i in range(n-1, -1, -1):
            leftProd[i] *= r
            r *= nums[i]
       
        return leftProd