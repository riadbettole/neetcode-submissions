class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        p1, p2 = 0, 0
        while p2 < len(prices):                
            if prices[p2] - prices[p1] > profit:
                profit = prices[p2] - prices[p1]
                p2 += 1
            elif prices[p2] < prices[p1]:
                p1 = p2
            else: 
                p2 += 1
            
        return profit