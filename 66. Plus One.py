class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ### use schoolbook addition with carry
        ### time complexity: O(n) one pass
        ### space complexity: O(1) for extra digits when all digits are 9
        for i in range(len(digits)-1, -1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        # we're here because all digits are nine
        return [1] + digits
