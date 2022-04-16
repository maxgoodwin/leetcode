class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    freqArr = [[] for i in range(len(nums) + 1)]
    freq = Counter(nums)
    
    for key, val in freq.items():
      freqArr[val].append(key)
    
    result = []
    
    for i in range(len(freqArr) - 1, 0, -1):
      for val in freqArr[i]:
        result.append(val)
      
      if len(result) == k: return result