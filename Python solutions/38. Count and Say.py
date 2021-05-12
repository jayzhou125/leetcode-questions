class Solution:
    # def say(self, s: str) -> str:
    #     i, j = 0, 0
    #     arr = []
    #     while j <= len(s):
    #         while j < len(s) and s[j] == s[i]:
    #             j+=1
    #         arr.append(str(j-i))
    #         arr.append(s[i])
    #         i = j
    #         j+=1
    #     return ''.join(arr)
    
    def countAndSay(self, n: int) -> str:
        # revursive 
        # time complexity: o(n)
        # space complexity: o(n)
        # if n == 1: 
        #     return "1"
        # else:
        #     return self.say(self.countAndSay(n-1))
        
        # iterative
        # time complexity: o(n)
        # space complexity: o(1)
        # result = "1"
        # i = 2
        # while i <= n:
        #     result = self.say(result)
        #     i+=1
        # return result
        
        # iterative fast run time, easier to understand  
        if n == 1 : return "1"
        result = "1"
        for _ in range(n-1):
            prev_char = result[0]
            count = 1
            temp_s = ""
            for cur_char in (result[1::]):
                if cur_char != prev_char:
                    temp_s += str(count) + prev_char
                    prev_char = cur_char
                    count = 1
                else:
                    count += 1
            temp_s += str(count) + prev_char
            result = temp_s
        return result
