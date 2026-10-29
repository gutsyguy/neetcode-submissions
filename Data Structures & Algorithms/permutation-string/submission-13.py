class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        s1_counter = [0] * 26
        s2_counter = [0] * 26

        for i in range(n):
            s1_counter[ord(s1[i]) - ord('a')] += 1

        l = 0
        for r in range(m):
            if r - l + 1 > n:
                s2_counter[ord(s2[l]) - ord('a')] -= 1
                l += 1
                
            s2_counter[ord(s2[r]) - ord('a')] += 1

            if s1_counter == s2_counter:
                return True
        
        return False
        