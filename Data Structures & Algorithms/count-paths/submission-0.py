class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        memo = {}
        
        def dfs(i, j):
            if i >= ROWS or j >= COLS:
                return 0
            elif i == ROWS-1 and j == COLS - 1:
                return 1

            if (i,j) in memo:
                return memo[(i,j)]

            memo[(i,j)] = dfs(i, j + 1) + dfs(i + 1, j)
            return memo[(i,j)] 
         
        return dfs(0, 0)

                