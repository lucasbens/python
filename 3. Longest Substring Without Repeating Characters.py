"""Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # two iterators i,j
        # i index + 1 of the first repetiting char
        for j in range(n):
            if s[j] in mp and i <= mp[s[j]]:
                i = mp[s[j]] +1

            ans = max(ans, j - i + 1)
            mp[s[j]] = j 

        return ans
