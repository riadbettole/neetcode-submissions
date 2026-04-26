from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashWords = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            hashWords[tuple(count)].append(word)
        return list(hashWords.values())

        # for word in strs:
        #     sortedWord = ''.join(sorted(word))
        #     hashWords[sortedWord].append(word)

        # return list(hashWords.values())