'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        l_needle = len(needle)
                
        
        for i in range(len(haystack)+1 - l_needle):
            
            if haystack[i:i+l_needle] == needle:
                return i
        
        return -1
                
