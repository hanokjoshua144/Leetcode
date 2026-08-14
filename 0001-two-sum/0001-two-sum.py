class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,nums in enumerate(nums):
            if target - nums in seen:
                return[seen[target-nums],i]
            seen[nums]=i
        