class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characters1 = {

        }

        characters2 = {

        }

        if len(s) != len(t):
            return False

        for char in s:
            if char in characters1:
                characters1[char] += 1
            else:
                characters1[char] = 0

        for char in t:
            if char in characters2:
                characters2[char] += 1
            else:
                characters2[char] = 0
        
        if characters1 == characters2:
            return True
        else:
            return False
        