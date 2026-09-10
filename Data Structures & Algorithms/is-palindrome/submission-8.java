class Solution {
    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length() - 1;

        while (l < r){
            while (!Character.isLetterOrDigit(s.charAt(l)) && l < r){
                l += 1;
            }
            while (!Character.isLetterOrDigit(s.charAt(r)) && l < r){
                r -= 1;
            }

            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))){
                return false;
            }
            l += 1;
            r -= 1;
        }
        
        return true;
    }
}
