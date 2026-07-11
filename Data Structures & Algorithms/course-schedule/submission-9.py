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

 
        # adj = defaultdict(list)
        # locks_remaining = [0] * numCourses

        # for course, prereq in prerequisites:
        #     adj[prereq].append(course)
        #     locks_remaining[course] += 1

        # q = deque([i for i in range(numCourses) if locks_remaining[i] == 0])

        # courses_taken = 0

        # while q:
        #     node = q.popleft()
        #     courses_taken += 1
            
        #     for neighbor in adj[node]:
        #         locks_remaining[neighbor] -= 1
        #         if locks_remaining[neighbor] == 0:
        #             q.append(neighbor)

        # return courses_taken == numCourses

