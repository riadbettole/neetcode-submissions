from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = Counter(nums)
        
        topLen = [[] for _ in range(len(nums) + 1)]
        
        for key, value in hashMap.items():
            topLen[value].append(key)

        res = []
        for item in reversed(topLen):
            for num in item:
                if len(res) < k:
                    res.append(num)

        return res
        #hashMap = Counter(nums)
        #listHashMap = list(hashMap.items())
        #sortedList = sorted(listHashMap, key=lambda x: x[1], reverse=True)
        #res = [item[0] for item in sortedList]
        #return res[:k]