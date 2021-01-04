class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if len(grid) == 0 or grid == None:
            return 0
    
        # helper method
        def dfs(i, j) -> int:
            if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[i]) - 1 or grid[i][j] == "0":
                return 0
        
            grid[i][j] = "0"
        
            dfs(i - 1, j) # check up 
            dfs(i + 1, j) # check down
            dfs(i, j - 1) # check left
            dfs(i, j + 1) # check rihgt
            
            return 1
        
        numOfIsland = 0  
