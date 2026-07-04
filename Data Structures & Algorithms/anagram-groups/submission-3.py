from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        
        for word in strs: 
            wordSorted = sorted(word)
            wordJoined = "".join(wordSorted)
            hashMap[wordJoined].append(word)

        result = []
        for lists in hashMap.values():
            result.append(lists)

        return result