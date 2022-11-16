'''
Given an integer numRows, return the first numRows of Pascal's triangle.

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]

'''


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:


        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return [[1],[1,1]]
        
        p_2 = [1,1]

        res = [[1], [1,1]]
        

        for j in range(numRows-2):
            new= [1]

            for i in range(len(p_2)-1):

                new.append(p_2[i]+p_2[i+1])


            new.append(1)
            res.append(new)
            p_2 = new
        
        return res

            
