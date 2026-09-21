class Solution {
    public boolean hasDuplicate(int[] nums) {
        boolean value = false;
        HashSet set = new HashSet();
        for (int i : nums) {
            if (set.contains(i)) {
                return true;
            }
            set.add(i);
        }
        return false;
    }
}