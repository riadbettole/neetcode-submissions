class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(current_str, opened, closed):
            if len(current_str) == 2 * n:
                res.append(current_str)
                return
            
            if opened < n:
                dfs(current_str + "(", opened + 1, closed)

            if closed < opened :
                dfs(current_str + ')', opened, closed + 1)

        dfs("", 0, 0) 
        return res