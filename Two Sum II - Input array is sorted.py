class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # first thought: hash map
        # num_map = {}
        # l = len(numbers)
        # for i in range(l):
        #     compliment = target - numbers[i]
        #     if compliment in num_map:
        #         return [num_map[compliment], i+1]
        #     else:
        #         num_map[numbers[i]] = i+1
        
        # since the list is sorted, we can use two pointer
        l = len(numbers)
        left = 0
        right = l - 1
        
        while left < right:
            sum_of_two = numbers[left] + numbers[right]
            if sum_of_two < target:
                left += 1
            elif sum_of_two > target:
                right -= 1
            else:
                return [left+1, right+1]
