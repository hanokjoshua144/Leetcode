class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        count = {}
        maximum = 0

        for right in range(len(nums)):
            count[nums[right]] = count.get(nums[right], 0) + 1

            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1

            maximum = max(maximum, right - left + 1)

        return maximum

