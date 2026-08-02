class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        maxL = 0

        for num in nums:
            if num-1 in seen:
                continue
            
            start = num
            currL = 1
            while (start+1) in seen:
                start += 1
                currL += 1
            maxL = max(currL, maxL)

        return maxL 