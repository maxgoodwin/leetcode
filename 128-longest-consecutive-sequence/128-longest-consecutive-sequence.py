class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    numSet = set(nums)
    result = 0
    
    for i in range(len(nums)):
      if nums[i] - 1 in numSet: continue
        
      consecutiveCount = 1
      checkNum = nums[i] + 1
      
      while checkNum in numSet:
        consecutiveCount += 1
        checkNum += 1
        
      result = max(consecutiveCount, result)
    
    return result