import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_chars = list(string.ascii_letters + string.digits)
        allowed_characters = set(alphanumeric_chars)

        left, right = 0, len(s) - 1

        while left < right:
            while left < right and s[left] not in allowed_characters:
                left += 1
            
            while left < right and s[right] not in allowed_characters:
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1

        return True
        
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))