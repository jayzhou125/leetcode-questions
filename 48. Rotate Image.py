# Java
class Solution {
    public void rotate(int[][] matrix) {
        // use extra space
        // int[][] result = new int[matrix.length][matrix[0].length];
        // for(int i = 0; i < matrix[0].length; i++){
        //     int k = 0;
        //     for(int j = matrix.length - 1; j >= 0; j--){
        //         // System.out.println(matrix[j][i]);
        //         result[i][k] = matrix[j][i];
        //         k++;
        //     }
        // }
        // System.out.println(Arrays.deepToString(result));
        
        // in-place
        // transpose then reflect, linear algebra
        // runtime: o(m)
        // space: o(1)
        transpose(matrix);
        reflect(matrix);        
    }
    
    public void transpose(int[][] matrix){
        int n = matrix.length;
        for (int i = 0; i < n; i++){
            for (int j = i; j < n; j++){
                int temp = matrix[j][i];
                matrix[j][i] = matrix[i][j];
                matrix[i][j] = temp;
            }
        }
        // System.out.println(Arrays.deepToString(matrix));
    }
    
    public void reflect(int[][] matrix){
        int n = matrix.length;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n/2; j++){
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][n-j-1];
                matrix[i][n-j-1] = temp;
            }
        }
        // System.out.println(Arrays.deepToString(matrix));
    }
}

# Python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # in-place
        self.transpose(matrix)
        self.reflect(matrix)
    
    def transpose(self, matrix):
        l = len(matrix)
        for i in range(l):
            for j in range(i, l):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]   
                
    def reflect(self, matrix):
        l = len(matrix)
        for i in range(l):
            for j in range(l//2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]  

