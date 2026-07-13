class Solution:
    # so the logic of dp is the we gonna create 
    # an array that says at each index how many coins
    # for the total dollar of i $ 
    # the final is gonna be the result
    # and for that for each i position, we just see the minimum
    # between the current iterations and the total of remainer + 1 coin 
    # because since we did a - c , we already put 1 coin
    def coinChange(self, coins: List[int], amount: int) -> int: 
        minCoins = [amount + 1] * (amount + 1)
        minCoins[0] = 0
        for a in range(1, len(minCoins)):
             for c in coins:
                if a - c >= 0:
                    minCoins[a] = min(minCoins[a], 1 + minCoins[a-c])                       
        return -1 if minCoins[-1] == amount + 1 else minCoins[-1]
        # cache = {}

        # def dfs(amount):
        #     if amount == 0:
        #         return 0  
        #     if amount in cache:
        #         return cache[amount] 

        #     res  = float("inf")
        #     for c in coins:
        #         if amount - c >= 0:
        #             res = min(res , dfs(amount - c) + 1)    
            
        #     cache[amount] = res 
        #     return res 

        # minCoins = dfs(amount) 
        # return -1 if minCoins == float('inf') else minCoins     