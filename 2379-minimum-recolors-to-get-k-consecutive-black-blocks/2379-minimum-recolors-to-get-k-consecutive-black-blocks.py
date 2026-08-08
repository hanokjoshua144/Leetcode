class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        colours = 0

        # Count white blocks in the first window
        for i in range(k):
            if blocks[i] == 'W':
                colours += 1

        mincolo = colours
        start = 1
        end = k

        while end < len(blocks):
            # Remove the leftmost block
            if blocks[start - 1] == 'W':
                colours -= 1

            # Add the new block
            if blocks[end] == 'W':
                colours += 1

            mincolo = min(mincolo, colours)

            start += 1
            end += 1

        return mincolo

        