class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(l, r):
            counter = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                r += 1
                l -= 1

                counter += 1

            return counter


            

            
        count = 0

        for i in range(len(s)):
            even = expand(i, i + 1)
            odd = expand(i, i)

            # count += 1

            count += even + odd 

        return count
        