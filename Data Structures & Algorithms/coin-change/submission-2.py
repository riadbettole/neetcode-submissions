class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: 

        cache = {}
        
        def dfs(amount):
            if amount == 0:
                return 0  
            if amount < 0:
                return float('inf')
            if amount in cache:
                return cache[amount] 

            min_path = float("inf")

            for c in coins:
                calc = dfs(amount - c) 
                if calc != float('inf'):
                    min_path = min(min_path, calc + 1)
            
            cache[amount] = min_path
            return min_path

        res = dfs(amount)  
        return res if res != float('inf') else -1     