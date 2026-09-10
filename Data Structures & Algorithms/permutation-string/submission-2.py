class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
            Understand:
                - s1 has to be a permutation meaning that if rearranged
                the characters in s1 can be found in s2.
                - Example 1 works because the substring cab is found which
                rearranged forms abc so this is true
                - Example 2 does not work because there is no substring that
                can be rearranged to form abc even though all the characters
                for it exist. 
            Match: I would use a sliding window approach with two pointers
            Plan:
                - Use a hashset to store all the characters in s1
                - Set both a left and right pointer equal to 0 and then move the
                right pointer until a character in s1_set has been found
                - Then set the left pointer equal to the right pointer and use a while
                loop to check to see if the character is in s1_set until either it is empty or 
                it the character is not in the hashset:
                    - If there hashset becomes empty then return True
                    - If the character isn't in the hashset then set the left pointer
                    back to the right pointer and then reinitilize the hashset to s1
                - If you reach the end, return if the hashset length is equal to 0.
        """

        s1_map = {}
        l = 0

        for c in s1:
            s1_map[c] = 1 + s1_map.get(c, 0)

        for r in range(len(s2)):
            if s2[r] in s1_map:
                l = r
                while l < len(s2) and s2[l] in s1_map:
                    s1_map[s2[l]] -= 1
                    if s1_map[s2[l]] == 0:
                        del s1_map[s2[l]]
                    l += 1
            if len(s1_map) == 0:
                return True
            else:
                s1_map = {}
                for c in s1:
                    s1_map[c] = 1 + s1_map.get(c, 0)

        return len(s1_map) == 0 
                

        # return True



