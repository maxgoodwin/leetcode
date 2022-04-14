class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    i=j=m=0
    while(j<len(s)):
      if (s[j]  in s[i:j]):
        while(i<j and s[j] in s[i:j]):
          i+=1
      j+=1
      m=max(m,j-i)
    return m