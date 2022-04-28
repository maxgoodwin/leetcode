class Solution:
  def isValid(self, s: str) -> bool:
    parenthesesStack = deque()
    openingParentheses = { '(': ')', '[': ']', '{': '}' }
    
    for parenthesis in s:
      if parenthesis in openingParentheses:
        parenthesesStack.append(parenthesis)
        continue
      
      if not parenthesesStack: return False
      
      popped = parenthesesStack.pop()
      
      if parenthesis != openingParentheses[popped]:
        return False
    
    return not parenthesesStack