class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # vertical scan 
        # time complexity: o(n) 
        # space complexity: o(1)
        # if strs == None or len(strs) == 0: return ""
        # for i in range(len(strs[0])):
        #     for j in range(len(strs)):
        #         if (i == len(strs[j]) or strs[j][i] != strs[0][i]): 
        #             return strs[0][:i]
        # return strs[0]
        
        # using zip in python 
        # Create one iterator per string using zip, it will stop at the shortest string
	# s is a tuple of characters at current position for each string
	# create a set to test unicity
        idx = 0
        for s in zip(*strs):
            if len(set(s)) != 1:
                break
            else:
                idx += 1
        return strs[0][:idx] if idx > 0 else ""


