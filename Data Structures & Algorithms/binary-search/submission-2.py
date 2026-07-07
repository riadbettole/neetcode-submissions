class Solution:
    def search(self, nums: List[int], target: int) -> int:
            l, r = 0, len(nums) - 1
            while l <= r:
                middleInd = int((r + l) / 2)
                if nums[middleInd] == target:
                    return middleInd
                elif nums[middleInd] > target:
                    r = middleInd - 1
                else:
                    l = middleInd + 1
            return -1