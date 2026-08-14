class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix = 1

        # Prefix: left → right
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1

        # Suffix: right → left
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
        