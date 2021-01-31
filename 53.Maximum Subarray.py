# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Constraints:
# 1 <= nums.length <= 3 * 104
# -105 <= nums[i] <= 105

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # first thought
#         local_max = nums[0];
#         global_max = nums[0];
        
#         for i in range(1, len(nums)):
#             local_max = max(nums[i], local_max + nums[i])
#             global_max = max(local_max, global_max)
            
#         return global_max

        # dynamic programming
        l = len(nums)
        max_sum = nums[0]
        
        for i in range(1, l):
            # compare with i-1, if i-1 < 0, nums[i] is the local max
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            if nums[i] > max_sum:
                max_sum = nums[i]
        return max_sum
