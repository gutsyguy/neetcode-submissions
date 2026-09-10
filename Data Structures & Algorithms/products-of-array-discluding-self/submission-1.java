class Solution {
    public int[] productExceptSelf(int[] nums) {
        /*
            The object is to output an array containing every number multiplied except the current index
            - The array has at least 2 numbers
            - the numbers range between -20 to 20

            Implementation plan:
            - Create a prefixes array to get the product of every number before the 
            index
            - Create a suffix array to get a multiple of all the numbers after the array
            - Crate an output array to multiple the prefixes and suffix arrays and return it
        */
        
        int[] prefixes = new int[nums.length];
        int[] suffixes = new int[nums.length];
        int[] res = new int[nums.length];

        int prefix = 1;
        int suffix = 1;

        // prefixes
        for (int i = 0; i < nums.length; i++){
            prefixes[i] = prefix;
            prefix *= nums[i];
        }

        //suffixes
        for (int j = 0; j < nums.length; j++){
            suffixes[nums.length - 1 - j] = suffix;
            suffix *= nums[nums.length - 1 - j];
        }

        for (int k = 0; k < nums.length; k++){
            res[k] = prefixes[k] * suffixes[k];
        }


        return res;
    }
}  
