class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        sum_range = self.prefix[right + 1] - self.prefix[left]

        return sum_range