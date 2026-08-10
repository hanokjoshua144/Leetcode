class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)

        left = 0
        total = 0
        minimum = float('inf')

        for right in range(len(cardPoints)):
            total += cardPoints[right]

            if right - left + 1 == len(cardPoints) - k:
                minimum = min(minimum, total)

                total -= cardPoints[left]
                left += 1

        return sum(cardPoints) - minimum
        