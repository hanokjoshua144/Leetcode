class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        count = 0
        depth = 0

        for i in range(len(s)):
            if s[i] == '(':
                depth += 1

            else:
                depth -= 1

                if s[i - 1] == '(':
                    count += 2 ** depth

        return count