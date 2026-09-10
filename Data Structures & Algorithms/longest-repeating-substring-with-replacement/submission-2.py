class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        longest = 0 
        res = 0
        l = 0

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            longest = max(freq[s[r]], longest) 
            
            while (r - l + 1) - longest > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1

            
            res = max(r - l + 1, res)

        return res


            # if (r - l + 1) - freq[s[r]] < k:
                

        