class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # First thought
        # if len(s) != len(t): return False
        # s_arr_sorted = sorted(list(s))
        # a_arr_sorted = sorted(list(t))
        # if str(s_arr_sorted) == str(a_arr_sorted):
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
