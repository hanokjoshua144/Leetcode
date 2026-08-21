class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            elif nums[mid] < target:
                if nums[left] == target:
                    return True
                else:
                    left += 1

                if nums[right] == target:
                    return True
                else:
                    right -= 1

            else:
                if nums[left] == target:
                    return True
                else:
                    left += 1

                if nums[right] == target:
                    return True
                else:
                    right -= 1

        return False