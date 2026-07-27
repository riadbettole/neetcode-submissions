class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(node, par):
            if node in visit:
                return False

            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n

        # newNode = set()
        # neighbors = set()
        # i = 1
        # for i in range(len(edges)):
        #     if edges[i][0] in newNode and edges[i][1] in neighbors:
        #         return False
        #     newNode.add(edges[i][0])             
        #     neighbors.add(edges[i][1])             
        # return True