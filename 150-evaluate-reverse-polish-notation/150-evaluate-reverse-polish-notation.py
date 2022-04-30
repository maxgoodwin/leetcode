class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
    if len(tokens) == 1: return tokens[0]
    
    operands = set({'+', '-', '*', '/'})
    intStack = deque()
    result = 0
    
    for char in tokens:
      if char not in operands:
        intStack.append(int(char))
        continue
      secondInt = intStack.pop()
      firstInt = intStack.pop()
      result = self.operate(firstInt, char, secondInt)
      intStack.append(result)
    
    return result
    
    
  def operate(self, first: int, operand: str, second: int) -> int:
    if operand == '+':
      return int(first + second)
    elif operand == '-':
      return int(first - second)
    elif operand == '*':
      return int(first * second)
    return int(first / second)