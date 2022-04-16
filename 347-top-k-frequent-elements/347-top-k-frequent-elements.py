class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    if len(nums) == k: return nums
    frequency = Counter(nums)
    
    while len(frequency) > k:
      keysToRemove = []
      for key in frequency:
        frequency[key] -= 1
        if frequency[key] == 0: keysToRemove.append(key)
        if len(frequency) == k: break
      
      for key in keysToRemove:
        frequency.pop(key)
        
    return frequency.keys()