from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        hashMap = Counter(s1)
        currWindow = Counter(s2[:len(s1)])
        
        if currWindow == hashMap:
            return True
            
        for r in range(len(s1), len(s2)):
            currWindow[s2[r]] += 1
            
            leftChar = s2[r - len(s1)]
            currWindow[leftChar] -= 1
            
            if currWindow[leftChar] == 0:
                del currWindow[leftChar]
                
            if currWindow == hashMap:
                return True

        return False