class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == None or len(matrix) == 0: return 0
        
        rows, cols = len(matrix), len(matrix[0])  
        print(rows, cols)
        dp = [[0]*(cols+1) for i in range(rows+1)]
        print(dp)
        max_l = 0 # max length for square
        
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i][j-1], \
                                   dp[i-1][j-1], \
                                   dp[i-1][j]) + 1
                    max_l = max(max_l, dp[i][j])
                # print(max_l)
        
        return max_l * max_l
