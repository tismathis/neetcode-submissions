class Solution {
    public int[] twoSum(int[] nums, int target) {
        int [] tab = nums;
        tab.sort();
        int i = 0 ;
        int j = nums.length-1;

        int [] final = new [2];

        while (i < nums.length || j > 0) {
            if (nums[i] + nums[j] == target) {
                final[0] = i;
                final[1] = j;
            }
            elif (nums[i] + nums[j] < target) {
                j--;
            }
            else {
                i++;
            }
        }
        return final;
    }
}
