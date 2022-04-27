class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    start = end = count = 0
    s1Chars = Counter(s1)
    currS2Chars = defaultdict(int)
    
    while end < len(s2):
      if s2[end] not in s1Chars:
        end += 1
        start = end
        currS2Chars = defaultdict(int)
        count = 0
        continue
      
      if currS2Chars[s2[end]] < s1Chars[s2[end]]: count += 1
      currS2Chars[s2[end]] += 1
      
      if count == len(s1): return True
      
      if end - start + 1 == len(s1):
        if s2[start] in s1Chars:
          if currS2Chars[s2[start]] <= s1Chars[s2[start]]: count -= 1
          currS2Chars[s2[start]] -= 1
        start += 1
      
      end += 1
    
    return False