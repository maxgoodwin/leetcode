class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        firstRow = False
        firstCol = False
        
        for row in range(len(matrix)):
          for column in range(len(matrix[0])):
            if matrix[row][column] == 0:
              if row != 0 and column != 0:
                matrix[row][0] = 0
                matrix[0][column] = 0
                
              if row == 0: firstRow = True
              if column == 0: firstCol = True
              
        for row in range(1, len(matrix)):
          for column in range(1, len(matrix[0])):
            if matrix[row][0] == 0 or matrix[0][column] == 0:
              matrix[row][column] = 0
        
        if firstCol:
          for row in range(len(matrix)):
            matrix[row][0] = 0
        if firstRow:
          for column in range(len(matrix[0])):
            matrix[0][column] = 0