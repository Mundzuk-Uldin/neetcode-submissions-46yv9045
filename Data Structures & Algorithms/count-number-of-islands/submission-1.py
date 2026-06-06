class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROWS, COLS = len(grid), len(grid[0])
    
        def sinkIsland(grid, r, c):
            offset = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr, dc in offset:
                row, col = r+dr, c+dc
                if min(row,col)<0 or row==ROWS or col==COLS or grid[row][col] == "0":
                    continue
                else:
                    grid[row][col] = "0"
                    sinkIsland(grid, row, col)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=="1":
                    count += 1
                    sinkIsland(grid, i, j)

        return count