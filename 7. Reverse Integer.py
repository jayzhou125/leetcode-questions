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
        # normal approach
        # x_abs_reverse = int(str(abs(x))[::-1])
        # if x_abs_reverse >= (2**31)-1: return 0 # 2**31 = 2147483648
        # return -1*x_abs_reverse if x < 0 else x_abs_reverse
    
        # use bit_length:
        x_abs_reverse = int(str(abs(x))[::-1])
        # if need more than 32 bits to represent, return 0
        if x_abs_reverse.bit_length() > 31: return 0 
        return -1*x_abs_reverse if x < 0 else x_abs_reverse
    
        
