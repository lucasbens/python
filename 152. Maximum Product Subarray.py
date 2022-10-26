'''
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) < 1:
            return 0
        
        # initialise with 1st value
        max_sub_max, sub_max, sub_min = nums[0],nums[0],nums[0]
        
        
        for n in nums[1:]:
            
            # keep sub_max before update
            temp = sub_max
            
            # keep track subarray with positive
            # if 0 we uptdate
            # if negative and sub_min negative we update sub_max (even number of positive)
            sub_max = max(n*sub_max, n*sub_min,n)
            
            # keep track subarray with odd nb of negative
            # if 0 we uptdate
            sub_min = min(n*temp, n*sub_min,n)
            
            max_sub_max = sub_max if sub_max>max_sub_max else max_sub_max
        
        return max_sub_max
        
        
