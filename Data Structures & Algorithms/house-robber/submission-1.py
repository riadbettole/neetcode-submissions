class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        for i in reversed(range(len(nums) - 3)):
            nums[i] = nums[i] + max(nums[i + 2], nums[i + 3])
        return max(nums[0], nums[1])

        # cache = {}
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     if i in cache:
        #         return cache[i]
        #     cache[i] = nums[i] + max(dfs(i+2), dfs(i+3)) 
        #     return cache[i]
        # return max(dfs(0), dfs(1))