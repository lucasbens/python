'''
You are given a positive integer array grades which represents the grades of students in a university.

Ordering following the conditions:

- The sum of the grades of students in the ith group is less than the sum of the grades of students in the (i + 1)th group, for all groups (except the last).

- The total number of students in the ith group is less than the total number of students in the (i + 1)th group, for all groups (except the last).


Return the maximum number of groups that can be formed.

'''



# image the grade are sort
# group 1 : 1 grade
# group 2 : 2 grades
# ...
# until the grades count in sum >= total number of grade 

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        c=0        
        for i in range(len(grades)):
            
            c+=i
            
            if c > len(grades):
                return i-1
            
            elif c == len(grades):
                return i
        
        return 1
            
        
        
            
            
