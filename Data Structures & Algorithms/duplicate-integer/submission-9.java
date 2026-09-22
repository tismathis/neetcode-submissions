public class Solution {
    public boolean hasDuplicate(int[] nums) {
       Set <Integer> seen = new HashSet<>();
       for (int num : nums) {
        if (seen.contains(num)) {
            return True;
        }
        else {
            seen.add(num);
        }
       }
       return false;
        
    }
