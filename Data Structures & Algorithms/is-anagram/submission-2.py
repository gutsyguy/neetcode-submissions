class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        if len(s) != len(t):
            return False

        for char in s:
            dict1[char] = 1 + dict1.get(char, 0)
        
        for char in t:
            dict2[char] = 1 + dict2.get(char, 0)

        return dict1 == dict2 