class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = self.binarySearch([row[0] for row in matrix], target)
        j = self.binarySearch(matrix[i], target)

        return matrix[i][j] == target

    def binarySearch(self, nums, target):
        l, r = 0, len(nums) - 1
        m = (r + l) // 2
        while l <= r :
            m = (r + l) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return r