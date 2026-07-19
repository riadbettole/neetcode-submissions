class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp

        # cache  = {}
        # result = [0] * (n + 1)
        # for i in range(n+1):
        #     binNum = bin(i)[2:]
        #     cache[binNum] = 0
        #     curr, binNumCurr = 0, binNum
        #     while len(binNumCurr) > 0:
        #         if binNumCurr[1:] in cache:
        #             curr += cache[binNumCurr[1:]]
        #             binNumCurr = binNumCurr[:-len(binNumCurr[1:])]
        #         if binNumCurr[-1] == '1':
        #             curr += 1
        #             binNumCurr = binNumCurr[:-1]
        #     cache[binNum] = curr
        #     result[i] = curr
        # return result