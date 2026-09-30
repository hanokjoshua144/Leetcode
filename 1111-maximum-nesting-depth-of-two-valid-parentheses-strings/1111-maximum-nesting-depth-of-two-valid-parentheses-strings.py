class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        depth = 0
        stack = []

        for ch in seq:
            if ch == '(':
                
                stack.append(depth % 2)
                depth += 1
            else:
                depth -= 1
                stack.append(depth % 2)
                

        return stack