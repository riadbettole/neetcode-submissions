from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord('a') - ord(c)] += 1
            res[tuple(count)].append(word)
        return list(res.values())

        #res = defaultdict(list)
        #for word in strs: 
        #    sortedS = "".join(sorted(word))
        #    hashMap[sortedS].append(word)
        #return list(hashMap.values())