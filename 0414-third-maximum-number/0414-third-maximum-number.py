class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        new1 = []

        nums.sort()

        for i in range(len(nums)):
            if nums[i] not in new1:
                new1.append(nums[i])

        if len(new1) >= 3:
            return new1[-3]
        else:
            return new1[-1]