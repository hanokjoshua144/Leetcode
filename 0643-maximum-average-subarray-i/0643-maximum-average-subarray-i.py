class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = 0

        # First window
        for i in range(k):
            total += nums[i]

        max_avg = total / k

        start = 1
        end = k

        while end < len(nums):
            total = total - nums[start - 1] + nums[end]
            avg = total / k
            max_avg = max(max_avg, avg)

            start += 1
            end += 1

        return max_avg