class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for ch in num:
            while len(stack) > 0 and k > 0 and stack[-1] > ch:
                stack.pop()
                k -= 1

            stack.append(ch)

        if k > 0:
            stack = stack[:-k]

        result = ''.join(stack)

        result = result.lstrip('0')

        if result == '':
            return '0'

        return result