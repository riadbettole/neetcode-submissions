class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r
        while l <= r:
            m = (l + r) // 2
            temp = 0
            
            for b in piles:
                temp += math.ceil(b/m)
                
            if temp > h:
                l = m + 1
            else:
                k = m
                r = m - 1
        return k
