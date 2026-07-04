class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in previous:
                return [previous[diff], i]
            previous[num] = i