class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if (grid[ROWS-1][COLS-1] == 1 or grid[0][0] == 1):
            return -1
        queue = deque()
        visit = set()
        queue.append((0, 0))
        visit.add((0, 0))
        length = 1

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS-1 and c == COLS-1:
                    return length
                neighbors = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
                for dr, dc in neighbors:
                    row = dr + r
                    col = dc + c
                    if(min(row, col) < 0 or row == ROWS or col == COLS
                    or (row,col) in visit or grid[row][col] == 1):
                        continue
                    visit.add((row,col))
                    queue.append((row,col))
            length += 1
        return -1