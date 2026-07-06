from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        hashMap = Counter(s1)
        currWindow = Counter(s2[:len(s1)])
        
        for r in range(len(s1), len(s2)):
            if currWindow == hashMap:
                return True
            
            currWindow[s2[r]] += 1
            currWindow[s2[l]] -= 1
            
            if currWindow[s2[l]] == 0:
                del currWindow[s2[l]]

            l += 1
        return currWindow == hashMap