class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    start = end = maxFreqInRange = result = 0
    charsInCurrentRange = defaultdict(int)
    
    while end < len(s):
      charsInCurrentRange[s[end]] += 1
      
      maxFreqInRange = max(maxFreqInRange, charsInCurrentRange[s[end]])
      
      if end - start + 1 - maxFreqInRange > k:
        charsInCurrentRange[s[start]] -= 1
        start += 1
      else: result = max(result, end - start + 1)
      end += 1
      
    return result