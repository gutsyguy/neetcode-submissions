class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return r - l - 1

        start = 0
        length = 1

        left = 0
        right = 0

        for i in range(len(s)):
            even = expand(i, i + 1)
            odd = expand(i, i)

            if even > length:
                start = i
                length = even

                left = start - length // 2 + 1
                right = start + length // 2

            if odd > length:
                start = i
                length = odd

                left = start - length // 2
                right = start + length // 2 


        # print(left, right)
        return s[left: right + 1]

        