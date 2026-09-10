class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        
        stack = []

        if len(s) < 2:
            return False

        for char in s:
            if char in hashmap:
                if stack and stack[-1] == hashmap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return stack == []

                

        return stack == []