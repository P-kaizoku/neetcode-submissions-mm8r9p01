class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        mp = {}

        def dfs(i):
            if i >= n:
                return 0
            
            if i in mp:
                return mp[i]
            
            money = max(dfs(i+2) + nums[i], dfs(i+1))

            mp[i] = money

            return money
        
        return dfs(0)