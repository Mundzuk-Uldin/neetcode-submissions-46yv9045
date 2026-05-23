class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        ROWS, COLUMNS = len(grid), len(grid[0])
        def floodIsland(grid, r, c):
            nonlocal ROWS, COLUMNS
            if(r == ROWS or c == COLUMNS or min(r,c) < 0
            or grid[r][c] == "0"):
                return
            grid[r][c] = "0"
            floodIsland(grid, r-1,c)
            floodIsland(grid, r+1,c)
            floodIsland(grid, r,c-1)
            floodIsland(grid, r,c+1)

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "0":
                    continue
                counter += 1
                floodIsland(grid, r, c)

        return counter