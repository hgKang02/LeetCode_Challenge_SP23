class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        for i in range(0, len(mat), 1):
            print(mat[i][i])
            result += mat[i][i]
            result += mat[i][len(mat) - i - 1]
        
        if len(mat) % 2 != 0:
            result -= mat[len(mat) // 2][len(mat) // 2]
        
        return result