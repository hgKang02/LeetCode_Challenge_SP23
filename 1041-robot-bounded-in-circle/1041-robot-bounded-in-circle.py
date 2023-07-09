class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = 0
        y = 0
        dx = 0
        dy = 1
        for i in instructions:
            if i == "G":
                x += dx
                y += dy
            elif i == "L":
                temp = dx
                dx = dy
                dy = -temp
            elif i == "R":
                temp = dy
                dy = dx
                dx = -temp
        
        return (x == 0 and y == 0) or dy != 1
