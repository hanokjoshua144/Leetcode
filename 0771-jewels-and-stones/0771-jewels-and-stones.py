class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        seen=set(jewels)
        total = 0
        for chr in stones:
            if chr in seen:
                total +=1

        return total