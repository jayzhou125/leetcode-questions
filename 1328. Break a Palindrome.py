class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

#         # input check 
#         # if(palindrome != palindrome[::-1]):
#         #     return ""
        
        if(len(palindrome)==1):
            return ""
        
        # since palindrome, look at left half of the palindrome
        for i in range(len(palindrome)//2):
            # if found one char that is not "a", replace with "a" and return
            if palindrome[i] != "a": 
                return palindrome[:i] + "a" + palindrome[i+1:]
        
        # if out of the loop, means the palindrome is all consist of "a", eg."aaaaaa"
        # replace the last char with "b", to give the smallest lexicographical order
        return palindrome[:-1] + "b"
