class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        dom = 0
        counter = {}
        l = 0

        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r], 0)
            dom = max(dom, counter[s[r]])
            
            while (r - l + 1) - dom > k:
                counter[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest
                


        