class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        res = 0
        l = 0
        length = 0
        maxCount = 0
        maxChar = ''
        # the way we can go about it is to keep track of max how ? 2 ifs, if same character +1 if its another character does it have more ?
        for r in range(len(s)):
            mp[s[r]] = mp.get(s[r], 0) + 1
            if mp[s[r]] > maxCount:
                maxCount = mp[s[r]]
                maxChar = s[r]
            if length - maxCount >= k:
                mp[s[l]] -= 1
                length -= 1
                l += 1
                if maxChar == s[l]:
                    maxCount -= 1
            length += 1
            res = max(length, res)
        return res