class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def lin_rob(nums):

            n = len(nums)

            mp = {}

            def dfs(i):
                if i >= n:
                    return 0
                
                if i in mp:
                    return mp[i]
                

                money = max(nums[i]+dfs(i+2), dfs(i+1))

                mp[i] = money

                return money

            return dfs(0)

        n = len(nums)
        if n < 2:
            return nums[0]

        return max(lin_rob(nums[:n-1]), lin_rob(nums[1:])) 