class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    numSet = set()
    alreadyCheckedSet = set()
    result = 0
    
    for num in nums: numSet.add(num)
    for i in range(len(nums)):
      if nums[i] in alreadyCheckedSet: continue
      
      left = nums[i] - 1
      right = nums[i] + 1
      consecutiveCount = 1
      
      while left in numSet:
        alreadyCheckedSet.add(left)
        consecutiveCount += 1
        left -= 1
        
      while right in numSet:
        alreadyCheckedSet.add(right)
        consecutiveCount += 1
        right += 1
      
      result = max(consecutiveCount, result)
    
    return result