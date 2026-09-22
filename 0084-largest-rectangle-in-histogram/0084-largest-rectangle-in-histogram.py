class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                maxArea = max(maxArea, height * width)

            stack.append(i)

        n = len(heights)

        while stack:
            height = heights[stack.pop()]

            if stack:
                width = n - stack[-1] - 1
            else:
                width = n

            maxArea = max(maxArea, height * width)

        return maxArea