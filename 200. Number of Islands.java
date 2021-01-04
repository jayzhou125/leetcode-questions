class Solution {
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        
        int numOfIsland = 0;
        for (int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[i].length; j++){
                if (grid[i][j] == '1'){
                    numOfIsland += dfs(grid, i, j);
                }
            }
        }
        return numOfIsland;
    }
    
    private int dfs(char[][] grid, int i, int j){
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[i].length || grid[i][j] == '0')
            return 0;
        
        grid[i][j] = '0';
        dfs(grid, i+1, j); // check down 
        dfs(grid, i-1, j); // check up
        dfs(grid, i, j-1); // check left
        dfs(grid, i, j+1); // check right

        return 1;
    }
    
}
