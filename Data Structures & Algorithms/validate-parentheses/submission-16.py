class Solution:
    def isValid(self, s: str) -> bool:
        closing_tag = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []

        for c in s:
            if c in closing_tag and stack and stack[-1] == closing_tag[c]:
                stack.pop()
            else:
                stack.append(c)

        return stack == []
        