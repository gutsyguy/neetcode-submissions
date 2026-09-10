import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_chars = list(string.ascii_letters + string.digits)
        allowed_characters = set(alphanumeric_chars)

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and s[l] not in allowed_characters:
                l += 1
            while l < r and s[r] not in allowed_characters:
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l, r = l + 1, r - 1
        return True