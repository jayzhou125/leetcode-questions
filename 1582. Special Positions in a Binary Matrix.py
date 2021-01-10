class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int: 
        # naive approach, two pass, o(2n)
#         rows = len(mat)
#         cols = len(mat[0])
        
#         row_sum = [0] * rows
#         col_sum = [0] * cols
        
#         # first pass, get sum for each row and column
#         for i in range(rows):
#             for j in range(cols):
#                 if mat[i][j] == 1:    
#                     row_sum[i] += 1
#                     col_sum[j] += 1
#         # print(row_sum)
#         # print(col_sum)
        
#         # second pass find the special positions
#         res = 0
#         for i in range(rows):
#             for j in range(cols):
#                 if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
#                     res += 1
#         return res

        # faster run time O(n + k), less memory too
        col_idx = set()
        for i in range(len(mat)): # loop through rows
            if sum(mat[i]) == 1:    # if the rows sum is 1
                col_idx.add(mat[i].index(1))    # add colum index to be checked
                
        res = 0
        for i in col_idx:
            temp = 0
            for j in range(len(mat)):
                # temp.append(mat[j][i])
                temp += mat[j][i]    
            if temp == 1:
                res += 1

        return res
