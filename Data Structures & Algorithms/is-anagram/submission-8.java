class Solution {
    public boolean isAnagram(String s, String t) {
        char[] newS = s.toCharArray();
        Arrays.sort(newS);
        char[] newT = t.toCharArray();
        Arrays.sort(newT);
        return Arrays.equals(newT, newS);
    }
}
