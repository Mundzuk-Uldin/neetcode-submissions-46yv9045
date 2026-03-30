class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix) -1
        while L <= R:
            M = (L + R)//2
            Top = matrix[M][-1]
            Bottom = matrix[M][0]
            if Top == target or Bottom == target:
                return True
            elif target < Top and target > Bottom:
                l = 0
                r = len(matrix[M]) -1
                while l <= r:
                    m =(l+r)//2
                    if target > matrix[M][m]:
                        l = m+1
                    elif target < matrix[M][m]:
                        r = m-1
                    else:
                        return True
                return False
            else:
                if target > Top:
                    L = M + 1
                elif target < Bottom:
                    R = M - 1
                else:
                    return False
        return False