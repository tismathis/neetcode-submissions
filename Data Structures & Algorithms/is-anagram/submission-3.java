class Solution {
    public boolean isAnagram(String s, String t) {
        Array newS = s.toCharArray()
        Arrays.sort(newS);
        Array newT = t.toCharArray();
        Arrays.sort(newT);
        if (s.lenght() != t.length()) {
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
