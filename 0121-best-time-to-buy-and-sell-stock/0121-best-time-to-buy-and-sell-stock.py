class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        maximum = 0

        for i in range(1, len(prices)):
            maximum = max(maximum, prices[i] - minimum)
            minimum = min(minimum, prices[i])

        return maximum
