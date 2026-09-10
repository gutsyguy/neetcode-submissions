class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
            AAABABB

            len(s) - most_frequent_element
            5 - 4 = 1

            XYYX
            len(s) - most_frequent_element
            4 - 2 = 2
        """
        l = 0
        longest = 0
        most_frequent = 0
        seen = {}

        for r in range(len(s)):
            seen[s[r]] = 1 + seen.get(s[r], 0) 
            most_frequent = max(most_frequent, seen[s[r]])
            
            while (r - l + 1) - most_frequent > k:
                seen[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

        return longest
        