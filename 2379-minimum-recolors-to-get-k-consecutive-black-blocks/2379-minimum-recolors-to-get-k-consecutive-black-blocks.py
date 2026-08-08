class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        colours = 0
        minimum = float('inf')

        for right in range(len(blocks)):
            if blocks[right] == 'W':
                colours += 1

            if right - left + 1 == k:
                minimum = min(minimum, colours)

                if blocks[left] == 'W':
                    colours -= 1

                left += 1

        return minimum