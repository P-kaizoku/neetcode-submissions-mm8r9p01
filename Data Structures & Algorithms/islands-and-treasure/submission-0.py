class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        m = len(grid)
        n = len(grid[0])

        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
        

        while q:
            x, y = q.popleft()

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                i, j = x+dx, y+dy

                if (0 <= i < m and 0 <= j < n) and grid[i][j] == inf:
                    grid[i][j] = grid[x][y] + 1
                    q.append((i, j))
        