class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        queue = deque()
        visit = set()
        queue.append((0, 0))
        visit.add((0, 0))
        length = 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS -1 and c == COLUMNS -1:
                    return length
                neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
                for rd, cd in neighbors:
                    row = rd + r
                    col = cd + c
                    if (min(row, col) < 0 or row == ROWS or 
                    col == COLUMNS or (row, col) in visit or 
                    grid[row][col] == 1):
                        continue
                    visit.add((row,col))
                    queue.append((row, col))
            length += 1
        return -1