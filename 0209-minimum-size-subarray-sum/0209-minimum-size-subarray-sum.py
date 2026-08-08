class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        total = 0
        minimum = float('inf')

        for right in range(n):
            total += nums[right]

            while total >= target:
                minimum = min(minimum, right - left + 1)

                total -= nums[left]
                left += 1
        
        if minimum == float('inf'):
            return 0

        return minimum