class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        islands = 0

        def bfs( grid, start):
            ROWS, COLS = len(grid), len(grid[0])
            nonlocal islands

            queue = deque()
            queue.append(start)
            visit.add(start)
            
            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()
      
                    neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    for dr, dc in neighbors:
                        newRow, newCol = r + dr, c + dc
                        if ((newRow < 0 or newCol < 0) or (newRow == ROWS or newCol == COLS) or
                            (newRow, newCol) in visit  or (grid[newRow][newCol] == "0") ):
                            continue
                        queue.append((newRow, newCol))
                        visit.add((newRow, newCol))
            islands += 1   

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visit and grid[i][j] == "1":
                    bfs(grid, (i, j))
        return islands 