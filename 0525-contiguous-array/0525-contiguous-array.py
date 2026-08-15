class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = {0: -1}
        prefix = 0
        maximum = 0

        for i, num in enumerate(nums):
            if num == 0:
                prefix -= 1
            else:
                prefix += 1

            if prefix in count:
                maximum = max(maximum, i - count[prefix])
            else:
                count[prefix] = i

        return maximum