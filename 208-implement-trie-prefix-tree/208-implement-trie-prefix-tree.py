class Trie:
  def __init__(self):
    self.children = [None] * 26
  
  def insert(self, word: str) -> None:
    currentChildren = self.children
    
    for i in range(len(word) - 1):
      alphabetPos = ord(word[i]) - 97
      
      if currentChildren[alphabetPos] == None:
        currentChildren[alphabetPos] = Node()
      
      currentChildren = currentChildren[alphabetPos].children
    
    lastCharPos = ord(word[-1]) - 97
    
    if currentChildren[lastCharPos] == None:
      currentChildren[lastCharPos] = Node()
      
    currentChildren[lastCharPos].wordEnd = True

  def search(self, word: str) -> bool:
    currentChildren = self.children
    
    for i in range(len(word) - 1):
      alphabetPos = ord(word[i]) - 97
      if currentChildren[alphabetPos] == None:
        return False
      
      currentChildren = currentChildren[alphabetPos].children
    
    lastCharPos = ord(word[-1]) - 97
    
    if currentChildren[lastCharPos] == None or not currentChildren[lastCharPos].wordEnd:
      return False
    
    return True

  def startsWith(self, prefix: str) -> bool:
    currentChildren = self.children
    
    for char in prefix:
      alphabetPos = ord(char) - 97
      
      if currentChildren[alphabetPos] == None:
        return False
      
      currentChildren = currentChildren[alphabetPos].children
    
    return True
      
class Node:
  def __init__(self):
    self.val = True
    self.wordEnd = False
    self.children = [None] * 26
      
      
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)