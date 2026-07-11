class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        courses = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            courses[crs].append(pre)

        def dfs(node):
            if node in visited:
                return False
            if courses[node] == []:
                return True

            visited.add(node)
                             
            for neighbor in courses[node]:
                if not dfs(neighbor): return False
                
            visited.remove(node) 

            courses[node] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

    def adjacencyList(self, edges) -> Dict : 
        adjList = {}
        for src, dst in edges:
            if src not in adjList:
                adjList[src] = []
            if dst not in adjList:
                adjList[dst] = []
            adjList[src].append(dst)
        return  adjList