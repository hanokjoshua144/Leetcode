class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for ch in s:
            if ch == '#':
                if len(stack1) > 0:
                    stack1.pop()
            else:
                stack1.append(ch)

        for ch in t:
            if ch == '#':
                if len(stack2) > 0:
                    stack2.pop()
            else:
                stack2.append(ch)

        if ''.join(stack1) == ''.join(stack2):
            return True
        else:
            return False