class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length

        for i in range(1, length):
            res[i] = res[i - 1] * nums[i - 1]

        rightProduct = 1
        for i in reversed(range(length)):
            res[i] *= rightProduct
            rightProduct *=  nums[i]
        return res 