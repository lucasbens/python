'''
Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.

 

Example 1:

Input: n = 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99

Example 2:

Input: n = 1
Output: 10

Example 3:
Explanation: 0,1,...,9

Input: n = 0
Output: 1
'''


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        if n==0:
            return 1
        
        
        p=9
        c=9
        tot = 10
        
        # if n>= 2
        # first digit btw [1-9]
        # next digits [0-9]
        # 9*9*8*...+
        for i in range(n-1):
            
            p*=c
            c-=1
            
            tot+=p
        
        return tot
