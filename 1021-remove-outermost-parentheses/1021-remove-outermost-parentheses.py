class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        stack = []

        for ch in s:
            if ch == '(':
                stack.append(ch)

                if len(stack) > 1:
                    result.append(ch)

            else:
                stack.pop()

                if len(stack) > 0:
                    result.append(ch)

        return ''.join(result)