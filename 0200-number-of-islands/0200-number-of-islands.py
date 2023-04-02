class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col, arr):
            num_row = len(arr)
            num_col = len(arr[0])
            
            if (row < 0 or col < 0 or row >= num_row or col >= num_col or arr[row][col] == "0"):
                return
            
            arr[row][col] = "0"
            dfs(row + 1 , col, arr)
            dfs(row - 1 , col, arr)
            dfs(row, col + 1, arr)
            dfs(row , col - 1, arr)
            
        
        if grid == None or len(grid) == 0:
            return 0
        count = 0
        num_row = len(grid)
        num_col = len(grid[0])
        for row in range(num_row):
            for col in range(num_col):
                if grid[row][col] == '1':
                    count += 1
                    dfs(row, col, grid)
        
        return count