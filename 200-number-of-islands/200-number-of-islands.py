class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    islandCount = 0
    
    for row in range(len(grid)):
      for col in range(len(grid[0])):
        if grid[row][col] == '1':
          self.bfs(grid, row, col)
          islandCount += 1
    
    return islandCount
          
  
  def bfs(self, grid: List[List[str]], startingRow, startingCol):
    queue = deque([(startingRow, startingCol)])
    
    while queue:
      row, col = queue.popleft()
      
      for rowCheck, colCheck in [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]:
        if rowCheck >= 0 and rowCheck < len(grid) and colCheck >= 0 and colCheck < len(grid[row]) and grid[rowCheck][colCheck] == '1':
          queue.append((rowCheck, colCheck))
          grid[rowCheck][colCheck] = '0'