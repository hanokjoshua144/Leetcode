class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        count = {0: -1}
        prefix = 0

        for i, num in enumerate(nums):
            prefix += num
            

            if prefix % k in count:
                if i - count[prefix % k] >= 2:
                    return True
            else:
                count[prefix % k] = i

        return False

        