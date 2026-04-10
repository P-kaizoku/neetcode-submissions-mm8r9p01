class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)

        max_length = 0

        for num in nums:
            if num-1 in st:
                continue
            current_num = num
            curr_len = 1
            while (current_num+1 in st):
                current_num += 1
                curr_len += 1
            max_length = max(max_length, curr_len)
        
        return max_length
            