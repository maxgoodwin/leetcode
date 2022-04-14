class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    result = start = end = 0
    
    charSet = set()
    while end < len(s): 
      if s[end] in charSet: 
        if end - start > result: result = end - start
          
        while s[start] != s[end]: 
          charSet.remove(s[start])
          start += 1
        
        charSet.remove(s[start])
        start += 1
        
        continue
      
      charSet.add(s[end])
      end += 1
      
    if end - start > result: result = end - start
      
    return result