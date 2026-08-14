class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefix = [0] * (len(arr) + 1)

        for i in range(len(arr)):
            prefix[i + 1] = prefix[i] + arr[i]

        total = 0

        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if (j - i + 1) % 2 == 1:
                    total += prefix[j + 1] - prefix[i]

        return total