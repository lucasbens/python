'''
There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.



Example 1:

Input: moves = "UD"
Output: true
Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.


Example 2:

Input: moves = "LL"
Output: false
Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.


'''


class Solution:
    def judgeCircle(self, moves: str) -> bool:

        # d = {'R': [1,0], 'L':[-1,0], 'U':[0,1], 'D': [0,-1] }

        # start = [0,0]
        # for m in moves:
        #     start=  [start[0]+d[m][0], start[1]+d[m][1]]
        
        # return start ==[0,0]

        p_x = 0
        p_y = 0

        for m in moves:

            if m == 'R':
                p_x += 1
            
            elif m == 'L':
                p_x -= 1

            elif m == 'U':
                p_y += 1

            elif m == 'D':
                p_y -=1
        
        return p_x== 0 and p_y== 0

