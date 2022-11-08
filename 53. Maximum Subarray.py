'''
Given an integer array nums, find the 
subarray
 which has the largest sum and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23



Solution (Kadane's Algorithm):

we iterate throw the array if the previous sum + new num < new num we start a new sum
|
|___> starting from new num => bigger sum

we keep tracking max a each iteration

'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums)>0:
            curr_sum_max = nums[0]
            sum_max = nums[0]

        for i in range(1,len(nums)):

            if nums[i] + curr_sum_max < nums[i]:
                curr_sum_max = nums[i]
            
            else:
                curr_sum_max += nums[i]

            
            sum_max= max(curr_sum_max,sum_max)
            
        return sum_max



