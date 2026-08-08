class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)

        left = 0
        right = k - 1
        count = 0

        while right < len(s):
            sub = int(s[left:left + k])

            if sub != 0 and num % sub == 0:
                count += 1

            left += 1
            right += 1

        return count