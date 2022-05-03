class Solution:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    days = [0] * len(temperatures)
    stack = []
    
    for currentDay, currentTemp in enumerate(temperatures):
      while stack and temperatures[stack[-1]] < currentTemp:
        previousDay = stack.pop()
        days[previousDay] = currentDay - previousDay
      stack.append(currentDay)
      
    return days