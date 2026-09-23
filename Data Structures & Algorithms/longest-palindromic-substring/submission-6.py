class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return r - l - 1

        l = 0
        r = 0

        start = 0
        length = 0

        for i in range(len(s)):
            even = expand(i, i + 1)
            odd = expand(i, i)

            if odd > length:
                start = i
                length = odd

                l = start - length // 2
                r = start + length // 2

            if even > length:
                start = i
                length = even

                l = start - length // 2 + 1
                r = start + length // 2 

        return s[l: r + 1]
        # return s[start: start + length]
        