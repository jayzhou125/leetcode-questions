class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # TLE 
        # nums_length = len(nums)
        # count = 0
        # temp = []
        # for i in nums:
        #     if i not in temp:
        #         temp.append(i)
        #         count += 1
        # if count != nums_length:
        #     return True
        # else:
        #     return False
        
        # sort, steady performance
        # if len(nums) == 1: return False
        # if len(set(nums)) == 1: return True
        # nums.sort()
        # for i in range(len(nums)-1):
            # if nums[i] == nums[i+1]:
                # return True
        # return False

        # use set in python or hashset in java to reduce cost for search 
        # num_set = set()
        # for num in nums:
        #     if num in num_set:
        #         return True
        #     else:
        #         num_set.add(num)
        # return False
        
        # python set solution
        num_set = set(nums)
        if len(num_set) != len(nums):
            return True
        else:
            return False
