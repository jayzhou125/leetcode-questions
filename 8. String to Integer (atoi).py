# Java
class Solution {
    public int myAtoi(String s) {
        int l = s.length();
        // base case
        if (l == 0) return 0;
        int idx = 0; 
        
        // step one
        while(idx < l && s.charAt(idx) == ' ')  idx++;
        
        // step two 
        int sign = 1;
        if (idx < l && (s.charAt(idx) == '-' || s.charAt(idx) == '+')){
            sign = s.charAt(idx) == '-' ? -1 : 1;
            idx++;
        }
        
        // step three
        int result = 0;
        while(idx < l && Character.isDigit(s.charAt(idx))){
            int digit = Character.getNumericValue(s.charAt(idx));
            if (result > (Integer.MAX_VALUE - digit)/10){ // overflow check 
                return sign == -1 ? Integer.MIN_VALUE : Integer.MAX_VALUE;
            }
            result = result * 10 + digit;
            idx++;
        }
        return sign * result;
    }
}

# Python
class Solution:
    def myAtoi(self, s: str) -> int:
        minint, maxint = -2 ** 31, 2 ** 31 - 1
        l = len(s)
        # base case
        if l == 0: return 0
        
        # step one
        i = 0
        while i < l and s[i] == ' ': 
            i += 1
            if i == l: return 0
     
        # step two
        sign = 1
        if s[i] == '-' : sign = -1
        if s[i] in "+-": i+=1

        # step three
        result = 0
        for char in s[i::]:
            if char.isdigit():
                digit = int(char)
                if result > (maxint - digit)//10:
                    if sign == -1 : return minint
                    if sign == 1 : return maxint
                result = result * 10 + digit
            else: break
        return sign * result
