
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        s = len(nums)
        result = 0

        for i in range(len(nums)):
            if s % (i + 1) == 0:
                result += nums[i] ** 2

        return result


            
        