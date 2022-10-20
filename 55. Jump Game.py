'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

'''




class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        last_good_index = len(nums)-1
        
        # backward traversal
        # keep im memory the last index allowing to traverse the array
        # if we are up to or equal the last_good_index we can reach the end of the array
        # reducing index of the last_good_index every time we can
        for i in range(last_good_index -1,-1,-1):
            
            if nums[i] + i >= last_good_index:
                last_good_index =i 
        
        return last_good_index == 0
            
            
            
