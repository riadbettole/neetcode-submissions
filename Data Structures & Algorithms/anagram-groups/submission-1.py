from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashWords = defaultdict(list)

        for word in strs:
            sortedWord = ''.join(sorted(word))
            hashWords[sortedWord].append(word)

        return list(hashWords.values())