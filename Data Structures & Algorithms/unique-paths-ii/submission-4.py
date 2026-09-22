class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        prev = [0] * (COLS-1)
        prev.append(1)
        if obstacleGrid[ROWS-1][COLS-1] == 1:
            return 0
        for i in range(ROWS-1,-1,-1):
            curr = [0] * COLS
            if obstacleGrid[i][-1] != 1:
                curr[-1] = prev[-1]
            for j in range(COLS-2,-1,-1):
                if obstacleGrid[i][j] == 1:
                    curr[j] = 0
                    continue
                curr[j] = curr[j+1] + prev[j]
            prev = curr
        return curr[0]
