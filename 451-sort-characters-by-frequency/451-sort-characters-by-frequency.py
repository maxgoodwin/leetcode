class Solution:
  def frequencySort(self, s: str) -> str:
    result = ''
    charFreq = Counter(s)
    frequencyArr = [None] * (len(s) + 1)
    
    for char, count in charFreq.items():
      if frequencyArr[count] == None:
        frequencyArr[count] = []
        
      frequencyArr[count].append(char)
      
    for i in range(len(frequencyArr) - 1, -1, -1):
      if frequencyArr[i] == None: continue
      
      for char in frequencyArr[i]:
        result += char * i
    
    return result