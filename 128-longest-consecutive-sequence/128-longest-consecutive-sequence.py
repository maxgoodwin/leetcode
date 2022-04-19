class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    numSet = set(nums)
    result = 0
    
    for num in nums:
      if num - 1 in numSet: continue
        
      consecutiveCount = 1
      checkNum = num + 1
      
      while checkNum in numSet:
        consecutiveCount += 1
        checkNum += 1
        
      result = max(consecutiveCount, result)
    
    return result