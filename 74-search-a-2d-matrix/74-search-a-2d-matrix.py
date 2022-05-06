class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    return self.binarySearchMatrix(matrix, target, 0, len(matrix) * len(matrix[0]) - 1)
  
  def binarySearchMatrix(self, matrix: List[List[int]], target: int, left: int, right: int) -> bool:
    if left > right: return False
    
    middle = (left + right) // 2
    
    col = middle % len(matrix[0])
    row = middle // len(matrix[0])
    
    if matrix[row][col] == target: return True
    
    return self.binarySearchMatrix(matrix, target, middle + 1, right) if target > matrix[row][col] else self.binarySearchMatrix(matrix, target, left, middle - 1)