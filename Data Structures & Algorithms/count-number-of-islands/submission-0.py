class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        dire = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(i, j):
            if  i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == "0":
                return
            
            grid[i][j] = "0"

            for d in dire:
                x = i + d[0]
                y = j + d[1]

                dfs(x, y)
        
        m = len(grid)
        n = len(grid[0])

        grps = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    grps += 1
        
        return grps
