class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        visited = set()

        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for num in nums:
                if num in visited:
                    continue
                
                subset.append(num)
                visited.add(num)

                dfs()

                subset.pop()
                visited.remove(num)
                
        dfs()
        return res