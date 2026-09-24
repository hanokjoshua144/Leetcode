class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s1 = sum(int(d) for d in str(nums[i]))
            
            if s1 == i:
                return i
        
        return -1