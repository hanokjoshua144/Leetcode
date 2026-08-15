class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = {0: 1}
        prefix = 0
        answer = 0

        for num in nums:
            prefix += num

            if prefix % k in count:
                answer += count[prefix % k]

            count[prefix % k] = count.get(prefix % k, 0) + 1

        return answer