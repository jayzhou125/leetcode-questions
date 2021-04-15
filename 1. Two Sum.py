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
        
# Java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hm = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            int complement = target - nums[i];
            if (hm.containsKey(complement)){
                return new int[] {hm.get(complement), i};
            }
            hm.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum sulotion");
    }
}
