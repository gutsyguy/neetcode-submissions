from collections import deque

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = [0] * 26

        for c in s1:
            s1_count[ord(c) - ord('a')] += 1

        l = 0 

        queue = deque()
        s2_count = [0] * 26

        for r in range(len(s2)):
            s2_count[ord(s2[r]) - ord('a')] += 1

            if r - l + 1 > len(s1):
                s2_count[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            if s2_count == s1_count:
                return True
        
        return False
                



       


