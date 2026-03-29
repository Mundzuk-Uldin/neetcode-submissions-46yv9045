from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grid = {}
        for i in range(len(board)):
            row = {}
            col = {}
            grid_id = 0
            if i % 3 == 0:
                grid = {}
            for j in range(len(board)):
                row_num = board[i][j]
                col_num = board[j][i]
                if (j % 3 == 0):
                    grid_id += 1
                if row_num.isdigit():
                    if row_num in row:
                        print("ROW ALREADY IN DIC")
                        return False
                    row[row_num] = 0
                    
                    #Calculate grids
                    if grid_id not in grid:
                        grid[grid_id] = {}
                    if row_num in grid[grid_id]:
                        print(f"{i},{j}")
                        print("ROW ALREADY IN GRID")
                        print(grid)
                        return False
                    grid[grid_id][row_num] = 0
                if col_num.isdigit():
                    if col_num in col:
                        print("COL ALREADY IN DIC")
                        return False
                    col[col_num] = 0
            print(grid)
            print(row)
            print(col)
            print("<<<<<<<<<<<>>>>>>>>>>>>>>>>")
        return True