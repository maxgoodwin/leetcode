class Solution:
  def maxArea(self, height: List[int]) -> int:
    volume = left = 0
    right = len(height) - 1
    
    while left < right:
      currentVolume = min(height[left], height[right]) * (right - left)
      volume = max(currentVolume, volume)
      if height[left] < height[right]: left += 1
      else: right -= 1
    
    return volume