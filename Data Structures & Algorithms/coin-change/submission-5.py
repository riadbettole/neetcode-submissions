class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: 

        cache = {}

        def dfs(amount):
            if amount == 0:
                return 0  
            if amount in cache:
                return cache[amount] 

            res  = float("inf")
            for c in coins:
                if amount - c >= 0:
                    res = min(res , dfs(amount - c) + 1)    
            
            cache[amount] = res 
            return res 

        minCoins = dfs(amount) 
        return -1 if minCoins == float('inf') else minCoins     