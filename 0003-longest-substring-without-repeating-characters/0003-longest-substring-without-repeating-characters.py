class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        total = 0
        maximum = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            total += 1
            maximum = max(maximum, right - left + 1)

        return maximum


        