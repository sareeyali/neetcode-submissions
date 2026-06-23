class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        rowZero = False

        # which rows/cols need to be zeroed
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        # zero out all but first row/col
        for r in range(1, n):
            for c in range(1, m):
                if (matrix[0][c] == 0
                or matrix[r][0] == 0):
                    matrix[r][c] = 0

        # zero out first row/col
        if matrix[0][0] == 0:
            for r in range(n):
                matrix[r][0] = 0
            
        if rowZero:
            for c in range(m):
                matrix[0][c] = 0
