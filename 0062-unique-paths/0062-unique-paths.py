class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [0] * (n * m)
            
        for i in range(m):
            grid[i * n] = 1
        for j in range(n):
            grid[j] = 1
        for i in range(n ,m * n):
            index = 0
            if grid[i] == 1:
                continue
            else:
                index = (i//n - 1) * n + (i % n)
                grid[i] = grid[index] + grid[i - 1]
        
        return grid[m * n - 1]
                
        
        