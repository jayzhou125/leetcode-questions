import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # TLE because time complecity of O(l * k), nearly O(n^2)
#         l = len(nums)
#         ans = []
#         if l * k == 0: # if length of nums or k is 0, return an empty list 
#             return []
        
#         # there's l-k+1 sliding windows
#         for i in range(l-k+1):
#             ans.append(max(nums[i:i+k]))
#         return ans
    
        # using deque 
        d = collections.deque()
        res = []
        for i, val in enumerate(nums):
            while d and val > nums[d[-1]]:
                d.pop()
            d.append(i)
            if d[0]==i-k:
                d.popleft()
            if i>=k-1:
                res.append(nums[d[0]])
        return res
