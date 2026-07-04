class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {}
        for i, num in enumerate(nums):
            substracted = target - num
            if substracted in previous:
                return [previous[substracted], i]
            previous[num] = i