class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def bfs( grid, start):
            ROWS, COLS = len(grid), len(grid[0])

            queue = deque()
            queue.append(start)

            grid[start[0]][start[1]] = 0

            area = 1

            while queue:
                r, c = queue.popleft()
    
                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbors:
                    newRow, newCol = r + dr, c + dc
                    if ((newRow < 0 or newCol < 0) or (newRow == ROWS or newCol == COLS) or
                        (grid[newRow][newCol] == 0) ):
                        continue
                    grid[newRow][newCol] = 0
                    queue.append((newRow, newCol))
                    area += 1
            
            return area
        
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    # dfs(grid, i, j)
                    res = max(res, bfs(grid, (i, j)))

        return res    