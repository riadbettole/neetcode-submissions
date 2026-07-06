class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        res = 0
        l = 0
        length = 0
        for r in range(len(s)):
            mp[s[r]] = mp.get(s[r], 0) + 1
            if length - max(mp.values()) >= k:
                mp[s[l]] -= 1
                length -= 1
                l += 1
            length += 1
            res = max(length, res)
        return res