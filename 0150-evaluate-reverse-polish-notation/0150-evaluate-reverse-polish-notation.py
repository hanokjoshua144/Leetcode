class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for ch in tokens:
            if ch == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)

            elif ch == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)

            elif ch == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)

            elif ch == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a / b))

            else:
                stack.append(int(ch))

        return stack[-1]