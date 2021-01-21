# Given an array nums of n integers where n > 1,  
# return an array output such that output[i] is equal 
# to the product of all the elements of nums except nums[i].

# Example:
# Input:  [1,2,3,4]
# Output: [24,12,8,6]

# Constraint: It's guaranteed that the product of the elements of any prefix          
# or suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not 
# count as extra space for the purpose of space complexity analysis.)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # first thought, TLE
#         import math
#         output = []
#         for i in range(len(nums)):
#             temp = nums[i]
#             product = nums.pop(i)
#             output.append(math.prod(nums))
#             nums.insert(i, temp)
        
#         return output
        
        # second thought, use division, runtime error for case: 0/0
#         import math
#         product_of_all = math.prod(nums)
#         output = []
#         for i in nums:
#             output.append(int(product_of_all / i))
        
#         return output
        
        # answer O(N)
        # l = len(nums)
        # L, R, output = [0] * l, [0] * l, [0] * l
        
#         # L saves all product from the left till index i 
#         L[0] = 1
#         for i in range(1, l):
#             L[i] = nums[i-1] * L[i-1]
        
#         R[l-1] = 1
#         for i in reversed(range(l-1)):
#             R[i] = nums[i + 1] * R[i + 1]
            
#         for i in range(l):
#             output[i] = L[i] * R[i]
        
#         return output
    
        # constant space O(N)
        l = len(nums)
        output = [0] * l
        
        output[0] = 1
        for i in range(1, l):
            output[i] = nums[i-1] * output[i-1]
            
        R = 1
        for i in reversed(range(l)):
            output[i] = output[i] * R
            R *= nums[i]
        
        return output
            
        
        
        

            
        
                
            
