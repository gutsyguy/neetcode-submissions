class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            odd = self.expand(i, i, s)
            even = self.expand(i, i + 1, s)

            res += (odd + even)

        return res
    
    
    
        
    def expand(self, l, r, s):
        counter = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

            counter += 1
        
        return counter

        
        