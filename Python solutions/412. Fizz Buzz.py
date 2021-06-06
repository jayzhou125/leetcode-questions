class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # naive approach
        # time complexity: o(n)
        # space complexity: o(n)
        # ans = []
        # for num in range(1, n+1):
        #     if num % 3 == 0 and num % 5 == 0: ans.append("FizzBuzz")
        #     elif num % 3 == 0: ans.append("Fizz")
        #     elif num % 5 == 0: ans.append("Buzz")
        #     else: ans.append(str(num))
        # return ans
        
        # string concatenation for neater code
        # ans = []
        # for num in range(1, n+1):
        #     s = ""
        #     if num % 3 == 0: s += "Fizz"
        #     if num % 5 == 0: s += "Buzz"
        #     if s == "": s = str(num)
        #     ans.append(s)
        # return ans
        
        # hashmap if there's too many mapping
        ans = []
        hm = {3:"Fizz", 5:"Buzz"}
        for num in range(1, n+1):
            s = ""
            for key in hm.keys():
                if num % key == 0: s += hm[key]
            if s == "": s += str(num)
            ans.append(s)
        return ans
