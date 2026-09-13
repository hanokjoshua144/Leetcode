class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newl = []

        for i in nums:
            if i not in newl:
                newl.append(i)

        for i in range(len(newl)):
            nums[i] = newl[i]

        return len(newl)