class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        newl = []

        for num in nums:
            if num != val:
                newl.append(num)

        for i in range(len(newl)):
            nums[i] = newl[i]

        return len(newl)