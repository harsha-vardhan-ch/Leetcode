class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        p=0
        def get(i,j):
            listofind=[(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            r=0
            for x,y in listofind: 
                if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y]==0:
                    r=r+1
            return r
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    p=p+get(i,j)
        return p