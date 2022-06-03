class Solution:
  def minOperations(self, logs: List[str]) -> int:
    depth = 0
    
    for log in logs:
      if log == './': continue
        
      if log == '../':
        depth = depth - 1 if depth > 0 else 0
        continue
      
      depth += 1
      
    return depth