class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return False
        # def dfs(i, target):
        #     if i >= len(nums):
        #         return target == 0
        #     if  target < 0:
        #         return False
        #     return dfs(i + 1, target) or dfs(i + 1, target - nums[i])
        # sumRes = sum(nums)
        # return dfs(0, sumRes/2) if sumRes % 2 == 0 else False