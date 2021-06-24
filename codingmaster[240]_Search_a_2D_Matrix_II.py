from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x,y = 0,0
        row, col = len(matrix), len(matrix[0])

        if row == col == 1:
            if matrix[0][0] == target:
                return True
            else:
                return False
        else:
            i = 0
            while (x < row-1) or (y < col-1):
                i += 1
                if target == matrix[x][y]:
                    return True
                else:
                    print(x,y)
                    if target >= matrix[x+1][y]:
                        x += 1
                    if target >= matrix[x][y+1]:
                        y += 1
                if i == 1000:
                    return print("BANG")

        return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],
[10,13,14,17,24],[18,21,23,26,30]]
target = 5

sol = Solution()
sol.searchMatrix(matrix, target)
