class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
        count = 1
        if fresh == 0:
            return 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in neighbors:
                    row = dr + r
                    col = dc + c
                    if(min(row, col)< 0 or row == ROWS or col == COLS or
                    grid[row][col] != 1):
                        continue
                    print(row,col)
                    fresh -= 1
                    if fresh == 0:
                        return count
                    grid[row][col] = 2
                    queue.append((row,col))
            count +=1
        return -1
