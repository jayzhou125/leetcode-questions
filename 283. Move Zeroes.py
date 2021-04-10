class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pointer
        # time complexity: O(n)
        # space complexity: O(1)
        idx_none_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[idx_none_zero] = nums[i]
                idx_none_zero += 1
        for idx in range(idx_none_zero, len(nums)):
            nums[idx] = 0
        
