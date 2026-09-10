class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> frequency1 = new HashMap();
        HashMap<Character, Integer> frequency2 = new HashMap();

        if (s.length() != t.length()){
            return false;
        }

        for (int i = 0; i < s.length(); i++){
            if (frequency1.containsKey(s.charAt(i))){
                frequency1.put(s.charAt(i), frequency1.get(s.charAt(i))+1);
            } else{
                frequency1.put(s.charAt(i), 1);
            }
            if (frequency2.containsKey(t.charAt(i))){
                frequency2.put(t.charAt(i), frequency2.get(t.charAt(i))+1);
            } else{
                frequency2.put(t.charAt(i), 1);
            }
        }

        System.out.println(frequency1);
        System.out.println(frequency2);

        return frequency1.equals(frequency2);

    }
}
