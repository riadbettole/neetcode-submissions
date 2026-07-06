from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        hashMap = Counter(s1)
        while l < len(s2) - len(s1) + 1:
            currWindow = Counter(s2[l: l + len(s1)])
            if currWindow == hashMap:
                return True
            l += 1
        return False