class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            seen = set()
            for j in range(9):
                e = board[i][j]
                if e == '.':
                    continue
                if e in seen:
                    return False
                seen.add(e)
            
            seen = set()
            for j in range(9):
                e = board[j][i]
                if e == '.':
                    continue
                if e in seen:
                    return False
                seen.add(e)
        
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()

                for i in range(3):
                    for j in range(3):
                        e = board[i + row][j + col]
                        if e == '.':
                            continue
                        if e in seen:
                            return False
                        seen.add(e)
        
        return True