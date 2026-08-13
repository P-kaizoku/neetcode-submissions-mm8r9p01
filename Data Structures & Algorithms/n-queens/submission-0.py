class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        board = [["."]*n for _ in range(n)]

        def isSafe(row, col):
            r = row-1

            while r >= 0:
                if board[r][col] == "Q":
                    return False
                r -= 1
            
            r, c = row-1, col-1

            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1
            
            r, c = row-1, col+1
            while r >= 0 and c < len(board):
                if board[r][c] == "Q":
                    return False
                
                r -= 1
                c += 1
            
            return True

            


        def backtrack(row):
            if row >= n:
                copy = ["".join(r) for r in board]
                res.append(copy)
                return
            

            for i in range(n):
                if isSafe(row, i):
                    board[row][i] = "Q"
                    backtrack(row+1)
                    board[row][i] = "."
                


        backtrack(0)
        return res
