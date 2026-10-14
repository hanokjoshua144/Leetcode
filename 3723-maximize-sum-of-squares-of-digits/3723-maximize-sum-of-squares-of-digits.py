
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num or sum == 0:
            return ""

        result = ""

        while sum >= 9:
            result += "9"
            sum -= 9

        if sum > 0:
            result += str(sum)

        while len(result) < num:
            result += "0"

        return result
