class Solution:
    def climbStairs(self, n: int) -> int:
        f, f1 = 1, 1
        for i in range(1, n):
            f, f1 = f1, f + f1
        return f1 
        # if n <= 2:
        #     return n
        # f = [0] * (n + 1)
        # f[1], f[2] = 1, 2
        # for i in range(3, n + 1):
        #     f[i] = f[i - 1] + f[i - 2]
        # return f[n]
        # cache = {}
        # def dfs(i):
        #     if i >= n:
        #         return i == n
        #     if i in cache:
        #         return cache[i]
        #     cache[i] = dfs(i + 1) + dfs(i + 2) 
        #     return cache[i]
        # return dfs(0)