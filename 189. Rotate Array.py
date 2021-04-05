class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # in case if k is bigger than the length of the list
        k = k % len(nums)
        
        # first reverse the whole string
        nums.reverse()
        
        # then reverse 0:k
        first_part = nums[0:k]
        first_part.reverse()
        nums[0:k] = first_part
        
        # lastly, reverse the rest of the string
        second_part = nums[k:]
        second_part.reverse()
        nums[k:] = second_part
