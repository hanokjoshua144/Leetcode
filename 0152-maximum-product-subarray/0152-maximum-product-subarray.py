class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        maximum = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            old_max = curr_max
            old_min = curr_min

            curr_max = max(x, old_max * x, old_min * x)
            curr_min = min(x, old_max * x, old_min * x)

            maximum = max(maximum, curr_max)

        return maximum