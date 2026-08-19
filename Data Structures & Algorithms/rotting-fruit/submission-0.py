class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        q = deque()


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 1))

        eta = 0
        while q:
            i, j, it = q.popleft()

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = dx+i, dy+j

                if (0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1):
                    eta = max(eta, it)
                    grid[ni][nj] = 2
                    q.append((ni, nj, it+1))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return eta