class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        arr = [0] * (COLS-1)
        arr.append(1)
        if obstacleGrid[ROWS-1][COLS-1] == 1:
            return 0
        for i in range(ROWS-1,-1,-1):
            if obstacleGrid[i][-1] == 1:
                arr[-1] = 0
            for j in range(COLS-2,-1,-1):
                if obstacleGrid[i][j] == 1:
                    arr[j] = 0
                    continue
                arr[j] = arr[j+1] + arr[j]
        return arr[0]