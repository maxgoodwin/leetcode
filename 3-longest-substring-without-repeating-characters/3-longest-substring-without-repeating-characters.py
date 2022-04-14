class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    result = i = 0
    strLen = len(s)
    
    while i < strLen - result:
      charSet = dict()
      count = 0
      
      while i < strLen and i < strLen - result + count:
        if s[i] in charSet: 
          i = charSet[s[i]] + 1
          break
        
        charSet[s[i]] = i
        count += 1
        i += 1
        
      if count > result: result = count
      
    return result