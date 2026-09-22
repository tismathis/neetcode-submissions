class Solution {
    public boolean isAnagram(String s, String t) {
        ArrayList newS = s.toCharArray();
        Arrays.sort(newS);
        ArrayList newT = t.toCharArray();
        Arrays.sort(newT);
        Arrays.equals(newT,newS);
}
