class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
      results = []
      
      for num in nums:
        absNum = abs(num)
        if (nums[absNum - 1] < 0): results.append(absNum)
        else: nums[absNum - 1] *= -1
        
      return results