class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        def bfs( grid, start):
            ROWS, COLS = len(grid), len(grid[0])

            queue = deque()
            queue.append(start)
            
            while queue:
                r, c = queue.popleft()
    
                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbors:
                    newRow, newCol = r + dr, c + dc
                    if ((newRow < 0 or newCol < 0) or (newRow == ROWS or newCol == COLS) or
                        (grid[newRow][newCol] == "0") ):
                        continue
                    queue.append((newRow, newCol))
                grid[r][c] = "0"

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    bfs(grid, (i, j))
                    islands += 1

        return islands 