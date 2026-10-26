class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for a in range(len(nums) - 2):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            b = a + 1
            c = len(nums) - 1

            while b < c:
                total = nums[a] + nums[b] + nums[c]

                if total == 0:
                    result.append([nums[a], nums[b], nums[c]])
                    b += 1
                    c -= 1

                    while b < c and nums[b] == nums[b - 1]:
                        b += 1

                    while b < c and nums[c] == nums[c + 1]:
                        c -= 1

                elif total < 0:
                    b += 1
                else:
                    c -= 1

        return result