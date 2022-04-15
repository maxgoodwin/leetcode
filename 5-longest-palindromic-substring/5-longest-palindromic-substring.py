class Solution:
  def longestPalindrome(self, s: str) -> str:
    start = end = 0
    
    for i in range(len(s)):
      len1 = self.expandFromMiddle(s, i, i)
      len2 = self.expandFromMiddle(s, i, i + 1)
      lenMax = max(len1, len2)
      
      if lenMax > end - start:
        start = i - (lenMax - 1) // 2
        end = i + lenMax // 2
  
    return s[start:end + 1]
  
  def expandFromMiddle(self, s: str, left: int, right: int) -> int:
    if not s or left > right: return 0
    
    while left >= 0 and right < len(s) and s[left] == s[right]:
      left -= 1
      right += 1
    
    return right - left - 1