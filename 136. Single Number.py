# from collections import defaultdict
# from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ### three ways to solve this using hash concept in python
        ### time complexity: O(n)
        ### space complexity: O(n)
        #1 use defaultdict from collections
        # hash_table = defaultdict(int)
        # for num in nums:
        #     hash_table[num] += 1
        # print(hash_table)
        # for item in hash_table:
        #     if hash_table[item] == 1:
        #         return item
        
        #2 use dict
        # hash_table = {}
        # for num in nums:
        #     if num in hash_table:
        #         hash_table[num] += 1
        #     else:
        #         hash_table[num] = 1
        # for item in hash_table:
        #     if hash_table[item] == 1:
        #         return item
        
        #3 use counter from collections
        # result = Counter(nums)    
        # for item in result:
        #     if result[item] == 1:
        #         return item
        
        ### use MathL: 2∗(a+b+c)−(a+a+b+b+c)=c
        ### time complexity: O(n) using sum
        ### space complexity: O(n) using set
        # return 2 * sum(set(nums)) - sum(nums)
        
        ### use XOR operater
        ### time complexity: O(n) one pass
        ### space complexity: O(1) since operation in place
        result = 0
        for num in nums:
            result ^= num
            
        return result

            
        
            
        
