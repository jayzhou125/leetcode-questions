# python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # one-line solution
        # s.reverse() 
        
        # two pointer
        # time complexity: o(n)
        # space complexity: o(1) in place
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1

            
# java
class Solution {
    public void reverseString(char[] s) {
        // time complexity: o(n)
        // space complexity: o(i) since in place
        int left = 0;
        int right = s.length - 1;
        while(left < right){
            char tmp = s[left];
            s[left] = s[right];
            s[right] = tmp;
            left++;
            right--;  
        }
    }
}
