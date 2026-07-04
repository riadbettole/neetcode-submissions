from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = Counter(nums)
        listHashMap = list(hashMap.items())
        sortedList = sorted(listHashMap, key=lambda x: x[1], reverse=True)
        res = [item[0] for item in sortedList]
        return res[:k]