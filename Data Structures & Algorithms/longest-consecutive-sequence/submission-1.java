class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet();
        int maxSubsequenceLength = 0;

        for (int num: nums){
            set.add(num);
        } 

        for (int num: nums){
            int counter = 1; 
            while (set.contains(num - 1)){
                counter += 1;
                num = num - 1;
            }
            if (counter > maxSubsequenceLength){
                maxSubsequenceLength = counter;
            }
        }

        return maxSubsequenceLength;
        
    }
}
