class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs: return ""

        res = ""
        for s in strs:
            res += str(len(s)) + ","
        res = res[:-1] + "#" + "".join(strs)
        return res
        # res = ""
        # for s in strs:
        #    res += str(len(s)) + "#" + s
        # return res

    def decode(self, s: str) -> List[str]:
        if not s: return []

        splitedS = s.split("#", 1)
        lengths = splitedS[0].split(",")
        encodedString = splitedS[1]
        index = 0
        res = []
        for length in lengths:
            res.append(encodedString[ index: index + int(length) ])
            index += int(length)
        return res
        # res = []
        # i = 0
        # while i < len(s):
        #     j = i
        #     while s[j] != "#":
        #         j += 1
        #     length = int(s[i:j])

        #     start_of_word = j + 1
        #     end_of_word = start_of_word + length

        #     res.append(s[start_of_word:end_of_word])
        #     i = end_of_word
        # return res
