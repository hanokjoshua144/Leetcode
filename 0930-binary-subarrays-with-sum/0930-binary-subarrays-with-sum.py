class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        count = {0: 1}
        prefix = 0
        answer = 0

        for num in nums:
            prefix += num

            if prefix - goal in count:
                answer += count[prefix - goal]

            count[prefix] = count.get(prefix, 0) + 1

        return answer
