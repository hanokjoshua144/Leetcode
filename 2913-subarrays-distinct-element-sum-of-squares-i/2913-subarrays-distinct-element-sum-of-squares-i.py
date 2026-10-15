class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0
        
        for i in range(len(nums)):
            s =set()
            for j in range(i,len(nums)):
                s.add(nums[j])
                dis=len(s)
                total += dis ** 2
        return total
