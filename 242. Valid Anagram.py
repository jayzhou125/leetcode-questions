# python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # First thought
        # if len(s) != len(t): return False
        # s_arr_sorted = sorted(list(s))
        # t_arr_sorted = sorted(list(t))
        # if str(s_arr_sorted) == str(t_arr_sorted):
        #     return True
        # return False

        # better solution, suppose have less memory and faster using java
        char_arr = [0] * 26
        # print(char_arr)
        ls = len(s)
        lt = len(t)
        if ls != lt: return False
        for i in range(ls):
            char_arr[ord(s[i]) - ord('a')] += 1
            char_arr[ord(t[i]) - ord('a')] -= 1
        
        for i in char_arr:
            if i != 0:
                return False
        
        return True
#java
class Solution {
    public boolean isAnagram(String s, String t) {
        // sorting
        // time complexity: o(nlogn)
        // space complexity: o(n)
        if (s.length() != t.length()) return false;
        char[] str1 = s.toCharArray();
        char[] str2 = t.toCharArray();
        Arrays.sort(str1);
        Arrays.sort(str2);
        return Arrays.equals(str1, str2);
    }
}
