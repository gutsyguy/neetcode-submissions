class Solution:
    def isValid(self, s: str) -> bool:
        
        """
            U: 
                - ensure that the string contains only valid parenthesis.
            P:
                - Use a hashmap and stack to map opening to closing brackets and store them in the stack, if the closing brackets are found then remove from stack
        """

        open_to_closing = {
            ")":"(",
            "}": "{",
            "]": "["
        }

        stack = []

        if not s:
            return True

        for c in s:
            if c not in open_to_closing:
                stack.append(c)
            elif c in open_to_closing:
                if stack and stack[-1] == open_to_closing[c]:
                    stack.pop()
                else:
                    return False

        return stack == []
        