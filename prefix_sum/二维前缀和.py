'''
presum[i][j]表示为从[0,0]到[i,j]的子矩形所有元素的和
presum[i][j] = presum[i-1][j] + presum[i][j-1] - presum[i-1][j-1] + matrix[i][j]

要求 [row1, col1][row1,col1] 到 [row2, col2][row2,col2] 的子矩形的面积的话
presum[row2][col2] - presum[row2][col1-1] - presum[row1-1][col2] + presum[row1-1][col1-1]
'''

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0]) if matrix else 0
        self.presum = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                self.presum[i+1][j+1] = self.presum[i+1][j] + self.presum[i][j+1] - self.presum[i][j] + matrix[i][j]




    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.presum[row2+1][col2+1] - self.presum[row2+1][col1] - self.presum[row1][col2+1] + self.presum[row1][col1]


#### 转换成一维前缀和
class NumMatrix:

        def __init__(self, matrix: List[List[int]]):
            m = len(matrix)
            n = len(matrix[0]) if matrix else 0

            self.presum = [[0] * (n+1) for _ in range(m)]

            for i in range(m):
                for j in range(n):
                    self.presum[i][j+1] = self.presum[i][j] +  matrix[i][j] 

        
        def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int: 
            total = 0
            for i in range(row1, row2+1):
                total += self.presum[i][col2+1] - self.presum[i][col1]
            return total

