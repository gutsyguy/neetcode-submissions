class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            char_list = [0] * 26

            for c in s:
                char_list[ord(c) - ord('a')] += 1

            char_list = tuple(char_list)

            if char_list in groups:
                groups[char_list].append(s)
            else:
                groups[char_list] = [s]

        return list(groups.values())

            
        