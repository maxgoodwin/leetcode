class Solution:
  def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    fleetStack = deque()
    positionSpeed = [(pos, speed) for pos, speed in zip(position, speed)]
    positionSpeed.sort(reverse=True)
    
    for posSpeed in positionSpeed:
      if not fleetStack or (target - posSpeed[0])/posSpeed[1] > (target - fleetStack[-1][0])/fleetStack[-1][1]:
        fleetStack.append(posSpeed)
    
    return len(fleetStack)