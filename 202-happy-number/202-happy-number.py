class Solution:
  def isHappy(self, n: int) -> bool:
    previousNums = set()
    currentNum = n
    
    while currentNum != 1:
      if currentNum in previousNums: return False
      previousNums.add(currentNum)
      
      currentSum = 0
      
      while currentNum > 0:
        currentDigit = currentNum % 10
        currentSum += currentDigit * currentDigit
        currentNum = math.floor(currentNum / 10)
      
      currentNum = currentSum
      
    return True