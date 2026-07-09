class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        ri = (m * n) - 1

        while l <= ri:
            m = l + (ri - l) // 2
            r = m // n
            c = m % n
            if target == matrix[r][c]:
                return True
            elif matrix[r][c] < target:
                l = m + 1
            else:
                ri = m - 1
        return False