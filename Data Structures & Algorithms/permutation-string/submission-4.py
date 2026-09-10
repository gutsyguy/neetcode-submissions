class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
            Understand: We are given two input strings, s1 and s2. We need to 
            find out if a rearranged version of s1 exists as a substring of s2.
            If this substring exists, return true otherwise return false.

            Considerations:
                - both strings only contain lowercase letters.

            Match: Sliding window

            Plan:
                - Set up a left and right pointer
                - Create two arrays of length 26 with 0s as the inital value
                    - Add 1 at index ord(s1[r]) - ord('a')
                    - Subtract 1 at index ord(s1[l]) - ord('a')
                - Move the right pointer until it at index len(s1) - 1.
                    - Add 1 at index ord(s2[r]) - ord('a')
                    - Subtract 1 at index ord(s2[l]) - ord('a')

                - If the two arrays are equal then return True
                - If you reach the end and they are not equal return false
        """

        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for c in s1:
            s1_count[ord(c) - ord('a')] += 1

        l = 0

        for r in range(len(s2)):
            s2_count[ord(s2[r]) - ord('a')] += 1

            if (r - l + 1) > len(s1):
                s2_count[ord(s2[l]) - ord('a')] -= 1
                l += 1

            if s1_count == s2_count:
                return True

        return False

    