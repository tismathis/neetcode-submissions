class Solution {
    public boolean isAnagram(String s, String t) {
        s = s.toCharArray.sort();
        t = t.sort();

        for (int i = 0 ; i < s.length() ; i++ ){
            if (!(s.charAt(i) == t.charAt(i))) {
                return false;
            }
        }
        return true;
    }
}
