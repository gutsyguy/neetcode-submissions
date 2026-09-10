class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        l = 0
        majority_count = 0
        longest = 0

        for r in range(len(s)):

            counter[s[r]] = 1 + counter.get(s[r], 0)
            majority_count = max(majority_count, counter[s[r]])

            while (r - l + 1) - majority_count > k:
                counter[s[l]] -= 1
                l += 1


            longest = max(longest, r - l + 1)

        return longest

            # if counter[s[r]] > majority_count:
            #     majority_count = counter
