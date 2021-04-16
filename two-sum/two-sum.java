class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] sumNums = new int[2];
        for (int i = 0; i < nums.length -1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    sumNums[0] = i;
                    sumNums[1] = j;
                    return sumNums;
                }
            }
        }

        return sumNums;
    }
}