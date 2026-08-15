class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = {0: 1}
        prefix = 0
        total = 0

        for num in nums:
            if num % 2 == 1:
                prefix += 1

            if prefix - k in count:
                total += count[prefix - k]

            count[prefix] = count.get(prefix, 0) + 1

        return total

        


        