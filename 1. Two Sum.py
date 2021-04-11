class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # one pass hashmap solution
        # time complexity: O(n)
        # space complexity: O(n)
        hmap = {}
        for i in range(len(nums)):
            complement = target - nums[i] 
            if complement in hmap:
                return [hmap[complement], i]
            hmap[nums[i]] = i
        return []
        
            
