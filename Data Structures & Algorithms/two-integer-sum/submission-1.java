class Solution {
    public int[] twoSum(int[] nums, int target) {
        int [] tab = new int[];
        for (int i = 0 ; i < nums.length(); i++) {
            for (int j = i+1 ; j < nums.length ; j++) {
                if (nums[i] + nums[j] = target) {
                    tab.add(i);
                    tab.add(j);
                }
            }
        }
        return tab;
    }
}
