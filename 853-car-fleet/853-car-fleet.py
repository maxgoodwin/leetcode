class Solution:
  def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    fleetStack = deque()
    positionSpeed = [0] * (max(position) + 1)
    
    for i in range(len(position)):
      positionSpeed[position[i]] = speed[i]
    
    fleetStack.append((len(positionSpeed) - 1, positionSpeed[-1]))
    
    for pos in range(len(positionSpeed) -2, -1, -1):
      if positionSpeed[pos] == 0: continue
      
      if (target - pos)/positionSpeed[pos] <= (target - fleetStack[-1][0])/fleetStack[-1][1]:
        continue
        
      fleetStack.append((pos, positionSpeed[pos]))
    
    return len(fleetStack)