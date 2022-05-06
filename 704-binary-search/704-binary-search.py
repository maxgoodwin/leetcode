class Solution:
  def search(self, nums: List[int], target: int) -> int:
    return self.binarySearch(nums, target, 0, len(nums) - 1)
    
  def binarySearch(self, nums: List[int], target: int, left: int, right: int) -> int:
    if left > right: return -1
    
    middle = (right + left) // 2
    
    if nums[middle] == target: return middle
    
    return self.binarySearch(nums, target, middle + 1, right) if target > nums[middle] else self.binarySearch(nums, target, left, middle - 1)
    