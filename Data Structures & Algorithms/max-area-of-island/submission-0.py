class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLUMNS = len(grid), len(grid[0])

        def areaOfIsland(grid, r, c):
            nonlocal ROWS, COLUMNS
            
            if (min(r,c) < 0 or r == ROWS or c == COLUMNS
            or grid[r][c] == 0):
                return 0

            grid[r][c] = 0
            counter = 1

            counter += areaOfIsland(grid, r-1, c)
            counter += areaOfIsland(grid, r+1, c)
            counter += areaOfIsland(grid, r, c-1)
            counter += areaOfIsland(grid, r, c+1)
            return counter

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 0:
                    continue
                newArea = areaOfIsland(grid, r, c)
                if maxArea < newArea:
                    maxArea = newArea
        return maxArea