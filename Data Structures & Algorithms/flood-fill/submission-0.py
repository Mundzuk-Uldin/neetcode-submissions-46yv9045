class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLUMNS = len(image), len(image[0])
        def dfs(image, sr, sc, starting, color):
            nonlocal ROWS, COLUMNS    

            if (sr == ROWS or sc == COLUMNS or
            min(sr,sc) < 0 or image[sr][sc] != starting or
            image[sr][sc] == color):
                return

            image[sr][sc] = color
            dfs(image, sr-1, sc, starting, color)
            dfs(image, sr+1, sc, starting, color)
            dfs(image, sr, sc-1, starting, color)
            dfs(image, sr, sc+1, starting, color)
            
        dfs(image,sr,sc,image[sr][sc], color)
        return image