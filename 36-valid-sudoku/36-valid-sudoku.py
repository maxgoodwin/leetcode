class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    rows = [set() for i in range(9)]
    columns = [set() for i in range(9)]
    squares = [set() for i in range(9)]
    
    for row in range(9):
      for col in range(9):
        if board[row][col] == '.': continue
        square = (row // 3) * 3 + (col // 3)
        
        if board[row][col] in rows[row] or board[row][col] in columns[col] or board[row][col] in squares[square]: return False
        
        rows[row].add(board[row][col])
        columns[col].add(board[row][col])
        squares[square].add(board[row][col])
    
    return True