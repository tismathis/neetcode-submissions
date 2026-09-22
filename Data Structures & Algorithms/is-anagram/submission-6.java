class Solution {
    public boolean isAnagram(String s, String t) {
        ArrayList newS = s.toCharArray();
        Arrays.sort(newS);
        ArrayList newT = t.toCharArray();
        Arrays.sort(newT);
        if (s.size() != t.size()) {
            return false;
        }
        for (int i = 0 ; i < s.length() ; i++ ){
            if (!(s.charAt(i) == t.charAt(i))) {
                return false;
            }
        }
        return true;
    }
}
