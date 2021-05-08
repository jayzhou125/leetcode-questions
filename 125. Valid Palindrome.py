#Java
class Solution {
    public boolean isPalindrome(String s) {
        // two pointer
        // check left and right
        // time complexity: o(n) one pass
        // space complexity: o(1) in place 
        for (int left = 0, right = s.length() - 1; left < right; left++, right--){
            while (left<right && !Character.isLetterOrDigit(s.charAt(left))){
                left++;
            }
            while (left<right && !Character.isLetterOrDigit(s.charAt(right))){
                right--;
            }
            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                return false;
            }
        }
        return true;
    }
}

# Python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer 
        # time: o(n)
        # space: o(1)
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum(): left += 1
            while left < right and not s[right].isalnum(): right -= 1
            if s[left].lower() != s[right].lower(): return False
            left += 1
            right -= 1
        return True
        # Note: 
        # Return Value from isalnum()
        # The isalnum() returns:
        # True if all characters in the string are alphanumeric
        # False if at least one character is not alphanumeric
