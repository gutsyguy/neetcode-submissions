class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0 
        maxLen = 0

        def expandAroundCenter(s, l, r):
            while l >= 0 and r < len(s) and s[r] == s[l]:
                l -= 1
                r += 1
            return r - l - 1

        for i in range(len(s)):
            even = expandAroundCenter(s, i, i+1)                
            odd = expandAroundCenter(s, i, i) 

            tempMax = max(even, odd)

            if tempMax > maxLen:
                maxLen = tempMax
                start = i - (maxLen - 1) // 2
                end = i + maxLen //2    

        return s[start:end+1]           