class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        noOfRemovals = i = 0
        
        while i < len(nums) - noOfRemovals:
            if nums[i] == val:
                nums[i] = nums[len(nums) - 1 - noOfRemovals]
                noOfRemovals += 1
            else:
                i += 1
                
        return len(nums) - noOfRemovals