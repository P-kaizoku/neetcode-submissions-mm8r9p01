class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxArr = nums[0]
        currSum = 0

        for i in nums:
            if currSum < 0:
                currSum =0
            currSum += i
            maxArr = max(maxArr, currSum)
        return maxArr