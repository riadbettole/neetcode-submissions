class Solution:
    def climbStairs(self, n: int) -> int:
        f, f1 = 1, 1
        for i in range(1, n):
            tmp = f1
            f1 = f + f1 
            f = tmp
        return f1 
        # cache = {}
        # def dfs(i):
        #     if i >= n:
        #         return i == n
        #     if i in cache:
        #         return cache[i]
        #     cache[i] = dfs(i + 1) + dfs(i + 2) 
        #     return cache[i]
        # return dfs(0)