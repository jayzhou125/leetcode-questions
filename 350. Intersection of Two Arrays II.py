from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ### using hash_map
        ### time complexity: O(n+m) n and m are the length of the arrays
        ### space complexity: O(min(n+m) + k) k is the final result 
        # hash_map = {}
        # if len(nums1) > len(nums2):
        #     list_to_loop = nums2
        #     other_list = nums1
        # else:
        #     list_to_loop = nums1
        #     other_list = nums2
        # for num in list_to_loop:
        #     if num in hash_map:
        #         hash_map[num] += 1
        #     else:
        #         hash_map[num] = 1
        # result = []
        # for num in other_list:
        #     if num in hash_map and hash_map[num] != 0:
        #         result.append(num)
        #         hash_map[num] -= 1
        # return result
        
        ### using sort
        ### time complexity: O(nlogn+mlogm), where nn and mm are the lengths of the arrays. We sort two arrays independently, and then do a linear scan.
        ### space complexity:  from O(logn+logm) to O(n+m), depending on the implementation of the sorting algorithm. For the complexity analysis purposes, we ignore the memory required by inputs and outputs.
        # nums1.sort()
        # nums2.sort()
        # i = 0
        # j = 0
        # k = 0
        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] < nums2[j]:
        #         i += 1
        #     elif nums1[i] > nums2[j]:
        #         j += 1
        #     else:
        #         nums1[k] = nums1[i]
        #         k += 1
        #         i += 1
        #         j += 1
        # return nums1[:k]
        
        ### using collections' built-in intersection(&)
        # detail about the API: https://www.geeksforgeeks.org/operations-on-python-counter/
        result = list((Counter(nums1) & Counter(nums2)).elements())
        return result

        
    
        
    
        
        
        
    
                
