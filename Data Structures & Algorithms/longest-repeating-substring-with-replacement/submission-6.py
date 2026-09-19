class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        candidates = {}
        counter = 0

        l = 0
        res = 0
        
        for r in range(len(s)):
            candidates[s[r]] = 1 + candidates.get(s[r], 0)
            counter = max(counter, candidates[s[r]] )

            while r - l + 1 - counter > k:
                candidates[s[l]] -= 1
                l += 1

            if (r - l + 1) - counter <= k:
                res = max(res, r - l + 1)

        return res

        