class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in reversed(range(len(cost) - 3)):
            cost[i] = cost[i] + min(cost[i + 2], cost[i + 1])
        return min(cost[0], cost[1])