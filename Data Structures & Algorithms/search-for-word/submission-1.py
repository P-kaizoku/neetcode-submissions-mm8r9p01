class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        direc = [(1,0), (-1,0), (0, 1), (0,-1)]
        def find(i, j, idx):
            if idx == len(word):
                return True

            if i < 0 or j < 0 or i >= m or j >= n or board[i][j]=="$":
                return False

            if board[i][j] != word[idx]:
                return False

            temp = board[i][j]
            board[i][j] = "$"

            for d in direc:
                if find(i+d[0], j+d[1], idx+1):
                    return True
            
            board[i][j] = temp
            return False




        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and find(i, j, 0):
                    return True
        
        return False