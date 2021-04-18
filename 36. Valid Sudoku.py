# Python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ### one pass
        ### time complexity O(1) since one pass over a board with 81 cells
        ### space complexity: O(1) a set with 81 string
        seen = set()
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num != ".":
                    found_in_row = str(num) + " in row:" + str(row)
                    found_in_col = str(num) + " in col:" + str(col)
                    found_in_box = str(num) + " in box:" + str(((row//3) * 3 + col//3))
                    if found_in_row in seen or found_in_col in seen or found_in_box in seen:
                        return False
                    else:
                        seen.add(found_in_row)
                        seen.add(found_in_col)
                        seen.add(found_in_box)
        return True


# java
class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Easy to remeber
        HashSet<String> hs = new HashSet<String>();
        for (int row = 0; row < 9; row++){
            for (int col = 0; col < 9; col++){
                char num = board[row][col];
                if ( num  != '.'){
                    if (!hs.add(num + "in row" + row) ||
                        !hs.add(num + "in col" + col) ||
                        !hs.add(num + "in box:" + ((row/3) * 3 + col/3))){
                        return false;
                    }
                }
            }
        }
        return true;
        
        // faster run time using bit masking
        // int[] rowA = new int[9];
        // int[] colA = new int[9];
        // int[][] matA = new int[3][3];
        // for (int i = 0; i < board.length; i++){
        //     for (int j = 0; j < board[0].length; j++){
        //         if (board[i][j] != '.'){
        //             int mask = 1 << (board[i][j] - '0');
        //             if ((rowA[i] & mask) == 0 && 
        //                 (colA[j] & mask) == 0 && 
        //                 (matA[i / 3][j / 3]   & mask) == 0){
        //                     rowA[i] ^= mask;
        //                     colA[j] ^= mask;
        //                     matA[i / 3][j / 3] ^= mask;
        //                 }
        //             else
        //                 return false;
        //         }
        //     }
        // }
        // return true;
    }
}
