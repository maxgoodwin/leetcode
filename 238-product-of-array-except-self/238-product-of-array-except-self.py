class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    productBefore = 1 
    productAfter = 1
    results = [1] * len(nums)
    
    for i in range(len(nums)):
      results[i] = productBefore
      productBefore *= nums[i]
    
    for i in range(len(nums) - 1, -1, -1):
      results[i] *= productAfter
      productAfter *= nums[i]
    
    return results