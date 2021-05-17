class Solution {
    public String longestCommonPrefix(String[] strs) {
        // one pass vertical scanning
        // time complexity: o(k + n) k is the lenfth of the first word, n is the length of strs 
        // space complexity: o(1) in place
        if (strs.length == 0 || strs == null) return ""; // edge case
        for (int i = 0; i < strs[0].length(); i++){
            // loop through each char in the first word
            for (int j = 1; j < strs.length; j++){
                // compare with every other str in strs
                if (i == strs[j].length() || strs[j].charAt(i) != strs[0].charAt(i)){
                    return strs[0].substring(0, i);
                }
            }
        }
        return strs[0];
    }
}
