class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = [0] * 26
        s2_counter = [0] * 26

        for c in s1:
            # s1_map[c] = 1 + s1_map.get(c,0)
            s1_counter[ord(c) - ord('a')] += 1

        l = 0

        for r in range(len(s2)):
            if r - l + 1 > len(s1):
                s2_counter[ord(s2[l]) - ord('a')] -= 1
                l += 1

            s2_counter[ord(s2[r]) - ord('a')] += 1

            if s1_counter == s2_counter:
                return True

        return False 
        