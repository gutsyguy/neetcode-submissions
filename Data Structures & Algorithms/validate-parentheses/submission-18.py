class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for c in s:
            if stack and c in match:
                if match[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return stack == []

        