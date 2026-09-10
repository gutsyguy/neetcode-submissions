class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_group = [0] * 26
        s2_group = [0] * 26

        for c in s1:
            s1_group[ord(c) - ord('a')] += 1

        l = 0
        for r in range(len(s2)):
            s2_group[ord(s2[r]) - ord('a')] += 1

            if r - l + 1 > len(s1):
                s2_group[ord(s2[l]) - ord('a')] -= 1
                l += 1

            if s1_group == s2_group:
                return True

        return False
        