class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        current_max = nums[0]
        maximum = nums[0]

        current_min = nums[0]
        minimum = nums[0]

        total = nums[0]

        for i in range(1, len(nums)):
            current_max = max(nums[i], current_max + nums[i])
            maximum = max(maximum, current_max)

            current_min = min(nums[i], current_min + nums[i])
            minimum = min(minimum, current_min)

            total += nums[i]

        if maximum < 0:
            return maximum

        return max(maximum, total - minimum)

        return maximum
        