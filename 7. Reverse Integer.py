# Java
class Solution {
    public int reverse(int x) {
        /*  
            For reference, 
            max integer value is  2147483647
            min integer value is -2147483648
        */ 
        int reverse = 0;
        while(x != 0){
            // pop the last digit
            int digit = x % 10;
            x /= 10;
            
            // Overflow check 
            if (reverse > Integer.MAX_VALUE/10 || (reverse == Integer.MAX_VALUE && digit > 7)) return 0;
            if (reverse < Integer.MIN_VALUE/10 || (reverse == Integer.MIN_VALUE && digit < -8)) return 0;
            
            // push back the digit 
            reverse = reverse * 10 + digit;
        }
        return reverse;
    }
}

# Python
class Solution:
    def reverse(self, x: int) -> int:
        x_abs = abs(x)
        x_abs = int(str(x_abs)[::-1])
        if x_abs > 2**31: return 0
        return -1*x_abs if x < 0 else x_abs
