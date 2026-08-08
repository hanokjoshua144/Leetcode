class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n

        if k == 0:
            return ans

        if k > 0:
            left = 0
            right = k

            size = sum(code[left:right + 1])

        else:
            left = n + k
            right = 0

            size = sum(code[left:n]) + code[0]

        for i in range(n):
            ans[i] = size - code[i]

            size -= code[left]
            left = (left + 1) % n

            right = (right + 1) % n
            size += code[right]

        return ans