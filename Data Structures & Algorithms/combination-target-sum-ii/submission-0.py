class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, subset = [], []
        
        def dfs(i, sum):
            if sum == target:
                res.append(subset.copy())
                return
                
            if i >= len(candidates) or sum > target:
                return
                
            subset.append(candidates[i])
            dfs(i + 1, sum + candidates[i])
            subset.pop()

            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(i + 1, sum)
                        
        dfs(0, 0)
        return res