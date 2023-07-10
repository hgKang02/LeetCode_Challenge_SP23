class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = "R"
        
        # 1,0   right
        # 0, -1 down
        # -1, 0 left
        # 0, 1 up
        result = []
        # dx = 1
        # dy = 0
        # x = 0
        # y = 0
        dic = {}
        dic["R"] = (0,1)
        dic["L"] = (0,-1)
        dic["U"] = (-1,0)
        dic["D"] = (1,0)
        x= 0
        y = 0
        dx = dic[direction][0]
        dy = dic[direction][1]
        while True:
            result.append(matrix[x][y])
            matrix[x][y] = "n"
            print(x, y)
            if len(result) == len(matrix) * len(matrix[0]):
                break
            if (direction == "D" and (x + dx == len(matrix) or matrix[x + dx][y] == "n")):
                direction = "L"
                dx = dic[direction][0]
                dy = dic[direction][1]
            elif (direction == "R" and (y + dy == len(matrix[0]) or matrix[x][y + dy] == "n")):
                direction = "D"
                dx = dic[direction][0]
                dy = dic[direction][1]
            elif (direction == "U" and (x + dx == -1 or matrix[x + dx][y] == "n")):
                direction = "R"
                dx = dic[direction][0]
                dy = dic[direction][1]
            elif (direction == "L" and (y + dy == -1 or matrix[x][y + dy] == "n")):
                direction = "U"
                dx = dic[direction][0]
                dy = dic[direction][1]
            x += dx
            y += dy
            print(dx, dy, direction, x, y)
        return result
    
    
    # 2 5
    # 8 4
    # 0 -1
            
                