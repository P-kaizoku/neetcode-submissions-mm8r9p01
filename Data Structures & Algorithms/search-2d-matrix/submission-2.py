class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        k = m*n

        l, r = 0, k-1

        while l <= r:
            mid = r - (r-l)//2

            row = mid//n
            col = mid%n

            e = matrix[row][col]

            if e == target:
                return True
            elif e < target:
                l = mid+1
            else:
                r = mid-1
        
        return False