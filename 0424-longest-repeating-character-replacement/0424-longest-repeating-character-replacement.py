class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maximum = 0
        count = {}

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            max_frequency = max(count.values())

            while (right - left + 1) - max_frequency > k:
                count[s[left]] -= 1
                left += 1

                max_frequency = max(count.values())

            maximum = max(maximum, right - left + 1)

        return maximum


        