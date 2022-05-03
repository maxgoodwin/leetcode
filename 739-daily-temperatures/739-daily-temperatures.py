class Solution:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    days = [0] * len(temperatures)
    hottestTemp = temperatures[-1]
    
    for currentDay in range(len(temperatures) - 2, -1, -1):
      if temperatures[currentDay] >= hottestTemp:
        hottestTemp = temperatures[currentDay]
        continue
      
      daysUntilHotter = 1
      while temperatures[currentDay + daysUntilHotter] <= temperatures[currentDay]:
        daysUntilHotter += days[currentDay + daysUntilHotter]
      
      days[currentDay] = daysUntilHotter
      
    return days