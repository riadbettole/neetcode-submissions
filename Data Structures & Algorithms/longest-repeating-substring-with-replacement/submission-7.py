class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        res = 0
        l = 0
        maxCount = 0

        for r in range(len(s)):
            mp[s[r]] = mp.get(s[r], 0) + 1
            maxCount = max(maxCount, mp[s[r]])
            if (r - l + 1) - maxCount > k:
                mp[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res