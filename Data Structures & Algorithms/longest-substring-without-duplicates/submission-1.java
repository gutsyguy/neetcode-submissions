class Solution {
    public int lengthOfLongestSubstring(String s) {
        int longest = 0;
        HashSet<Character> seen = new HashSet();
        int l = 0;

        for (int r = 0; r < s.length(); r++){
            while (seen.contains(s.charAt(r))){
                seen.remove(s.charAt(l));
                l++;
            }
            seen.add(s.charAt(r));

            if (seen.size() > longest){
                longest = seen.size();
            } 
        }

        return longest;
        
    }
}
