class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        vow = 0
        maximum = 0
        vowels = "aeiou"

        for right in range(len(s)):
            if s[right] in vowels:
                vow += 1

            if right - left + 1 > k:
                if s[left] in vowels:
                    vow -= 1
                left += 1

            maximum = max(maximum, vow)

        return maximum

            
        