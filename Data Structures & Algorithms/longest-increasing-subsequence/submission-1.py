class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in reversed(range(len(nums))):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)

        # cache = {}
        # def dfs(i):
        #     if  i >= len(nums):
        #         return 0
        #     if i in cache:
        #         return cache[i]
        #     longest = 1
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] > nums[i]:
        #             longest = max(longest, 1 + dfs(j))
        #     cache[i] = longest
        #     return cache[i]

        # res = 0
        # for i in range(len(nums)):
        #     res = max(res, dfs(i))

        # return res