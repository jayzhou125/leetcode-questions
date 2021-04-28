# python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # o(n^2) with o(1) space
        # exceed time limit
        # result = 0
        # for start in range(len(nums)):
        #     cur_sum = 0
        #     for end in range(start, len(nums)):
        #         cur_sum += nums[end]
        #         if cur_sum == k: 
        #             result += 1
        # return result
        
        # hashmap approach
        sum_map = {}
        sum_map[0] = 1
        result = 0
        cur_sum = 0
        for num in nums:
            cur_sum += num
            # if the sum between two indexes is k, 
            # that means we found a subarray that sums to k
            if (cur_sum-k) in sum_map:
                result += sum_map[cur_sum-k]
            if cur_sum in sum_map:
                sum_map[cur_sum] += 1
            else:
                sum_map[cur_sum] = 1
        return result
  
  # java
  class Solution {
    public int subarraySum(int[] nums, int k) {
        // easy to understand
        // o(n^2) runtime with o(1) space
        // int count = 0;
        // for(int start = 0; start < nums.length; start++){
        //     int sum = 0;
        //     for (int end = start; end < nums.length; end++){
        //         sum+=nums[end];
        //         if (sum == k){
        //             count++;
        //         }
        //     }
        // }
        // return count;
        
        // hashmap
        // time complexity: o(n) one pass
        // space complexity: o(n) creating a new map
        Map<Integer, Integer> sumMap = new HashMap<>();
        sumMap.put(0, 1); 
        int sum = 0;
        int result = 0;
        for (int i = 0; i < nums.length; i++){
            sum += nums[i];
            if (sumMap.containsKey(sum - k)){
                result += sumMap.get(sum - k);
            }
            sumMap.put(sum, sumMap.getOrDefault(sum, 0) + 1);
        }
        return result;
    }
}
