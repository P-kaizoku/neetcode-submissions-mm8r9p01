class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0
        m = len(grid)
        n = len(grid[0])

        def bfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return 0
            
            if grid[i][j] == 1:
                grid[i][j] = 0
                areaSum = 1
                for dx, dy in [(1,0), (-1,0), (0, 1), (0, -1)]:
                    areaSum += bfs(i+dx, j+dy)
                return areaSum

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 1:
                    maxArea = max(maxArea, bfs(i, j))
        
        return maxArea