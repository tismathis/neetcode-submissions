class Solution {
    public boolean hasDuplicate(int[] nums) {
        boolean value = false;
        Set set = new Set ();
        for int : i in nums {
            if set.contains(i) {
                return true;
            }
            set.add(i);
        }
        return false;
    }
}