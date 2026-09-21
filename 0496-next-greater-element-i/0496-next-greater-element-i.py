class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        result = {}

        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                result[smaller] = num

            stack.append(num)

        for num in stack:
            result[num] = -1

        return [result[num] for num in nums1]