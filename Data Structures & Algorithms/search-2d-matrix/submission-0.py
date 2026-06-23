class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0
        bot = ROWS - 1

        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break
        
        if not (top <= bot):
            return False
        
        mid = (top + bot) // 2

        lo = 0
        hi = COLS - 1

        while lo <= hi:
            half = (lo + hi) // 2
            if target < matrix[mid][half]:
                hi = half - 1
            elif target > matrix[mid][half]:
                lo = half + 1
            else:
                return True

        return False

        