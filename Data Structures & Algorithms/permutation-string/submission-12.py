class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0] * 26
        s2_count = [0] * 26

        for c in s1:
            s1_count[ord(c) - ord('a')] += 1

        l = 0
        n = len(s1)

        for r in range(len(s2)):
            if (r - l + 1) > n:
                s2_count[ord(s2[l]) - ord('a')] -= 1
                l += 1
            s2_count[ord(s2[r]) - ord('a')] += 1

            if s1_count == s2_count:
                return True

        return False 

        