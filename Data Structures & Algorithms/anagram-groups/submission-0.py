from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashWords = defaultdict(list)

        for i, word in enumerate(strs):
            sortedWord = ''.join(sorted(word))
            hashWords[sortedWord].append(word)

        final = []
        for key, pair in hashWords.items():
            final.append(pair)

        return final