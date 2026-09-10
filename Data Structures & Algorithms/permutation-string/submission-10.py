class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        l = 0

        count1 = [0] * 26
        count2 = [0] * 26

        for c in s1:
            count1[ord(c) - ord('a')] += 1

        for r in range(m):
            if (r - l + 1) > n:
                count2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            count2[ord(s2[r]) - ord('a')] += 1

            if count1 == count2:
                return True

        return False


        