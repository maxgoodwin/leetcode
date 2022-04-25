class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) == 1: return 1
    subStringChars = dict()
    result = count = i = 0
    
    for i in range(len(s)):
      if s[i] in subStringChars and subStringChars[s[i]] >= i - count:
        result = max(result, count)
        count = i - subStringChars[s[i]] - 1
      
      subStringChars[s[i]] = i
      count += 1
    
    return max(result, count)