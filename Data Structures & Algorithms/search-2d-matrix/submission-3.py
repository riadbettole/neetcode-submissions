class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, (ROWS * COLS) - 1
        
        while l <= r:
            m = (l + r) // 2
            mid_val = matrix[m // COLS][m % COLS]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                l = m + 1
            else:
                r = m - 1
                
        return False