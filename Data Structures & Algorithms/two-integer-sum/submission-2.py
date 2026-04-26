class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNums = {}
        for i, n in enumerate(nums):
            hashNums[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashNums and hashNums[diff] != i:
                return [i, hashNums[diff]]

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if j > i and nums[i] + nums[j] == target:
        #             return [i, j]