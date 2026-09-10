class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        most_frequent = 1
        frequency_map = {}
        longest_substring_len = 0

        l = 0
        for r in range(len(s)):
            frequency_map[s[r]] = 1 + frequency_map.get(s[r], 0)

            most_frequent = max(most_frequent, frequency_map[s[r]])

            while r - l + 1 - most_frequent > k:
                frequency_map[s[l]] -= 1
                l += 1

            longest_substring_len = max(longest_substring_len, r - l + 1)

            
        print(r - l + 1)

        return longest_substring_len

        
        