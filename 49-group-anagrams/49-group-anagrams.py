class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    sCharDict: dict[frozenset, list[str]] = dict()
    
    for s in strs:
      sSet: set[str] = set()
      sDict: dict[str, int] = dict()
      
      for char in s:
        if char not in sDict: sDict[char] = 0
          
        sDict[char] += 1
        sSet.add(char + str(sDict[char]))
      
      frozenSSet = frozenset(sSet)
        
      if frozenSSet not in sCharDict: sCharDict[frozenSSet] = [s]
      else: 
        lst = sCharDict[frozenSSet]
        lst.append(s)
        sCharDict[frozenSSet] = lst
        
    return sCharDict.values()