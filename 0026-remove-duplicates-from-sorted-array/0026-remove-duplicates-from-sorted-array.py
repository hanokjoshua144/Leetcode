class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newl = []

        for num in nums:
            if num not in newl:
                newl.append(num)

        for i in range(len(newl)):
            nums[i] = newl[i]

        return len(newl)