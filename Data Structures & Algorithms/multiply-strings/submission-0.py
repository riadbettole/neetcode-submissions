class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        num1, num2 = num1[::-1], num2[::-1]
        res = 0
        for i, c2 in enumerate(num2):
            n2 = int(c2) * (10 ** i)
            for j, c1 in enumerate(num1):
                n1 = int(c1) * (10 ** j)
                res += n1 * n2

        return str(res)