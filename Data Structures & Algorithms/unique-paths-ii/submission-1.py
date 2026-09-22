class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}
        def memoization(r,c):
            if r == ROWS or c == COLS:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0
            if r == ROWS-1 and c == COLS-1:
                return 1
            if (r,c) in memo:
                return memo[(r,c)]
            memo[(r,c)] = memoization(r+1,c) + memoization(r,c+1)
            return memo[(r,c)]
        return memoization(0,0)