class Solution {
    public int strStr(String haystack, String needle) {
        // sliding window with for loop
        // time complexity: o(n) one pass
        // space complexity: o(1) in place
        if (needle.length() == 0) return 0;
        int k = needle.length();
        for (int i = 0; i + k <= haystack.length(); i++){
            if (haystack.substring(i, i+k).equals(needle)) return i;
        }
        return -1;
        
        // sliding window using while loop, logic is the same
        // if (needle.length() == 0) return 0;
        // int k = needle.length();
        // int i = 0;
        // while (i + k <= haystack.length()){
        //     String temp_sub = haystack.substring(i, i + k);
        //     if (temp_sub.equals(needle)) return i;
        //     i++;
        // }
        // return -1;
    }
}