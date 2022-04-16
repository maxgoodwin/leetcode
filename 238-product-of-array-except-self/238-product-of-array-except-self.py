class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    productBefore = [1] * len(nums)
    productAfter = [1] * len(nums)
    results = [0] * len(nums)
    
    for i in range(1, len(nums)):
      productBefore[i] = nums[i - 1] * productBefore[i - 1]
    
    for i in range(len(nums) - 2, -1, -1):
      productAfter[i] = nums[i + 1] * productAfter[i + 1]
      
    print(productBefore)
    print(productAfter)
    
    for i in range(len(nums)):
      results[i] = productBefore[i] * productAfter[i]
      
    return results