class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [-1 for _ in range(n)]


        def dfs(step):
            if step == n:
                return 1
            
            if step > n:
                return 0
            
            if dp[step] != -1:
                return dp[step]
            
            dp[step] = dfs(step+1) + dfs(step+2)

            return dp[step]
            


        return dfs(0)
