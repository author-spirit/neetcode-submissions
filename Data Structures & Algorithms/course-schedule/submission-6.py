class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Invariant: If a course is completed only if its pre-requisites also completed without cycle
        State: Visiting (tri-state) - visiting, visited (fully completed)
        Termination: If course is still in progress then terminate (there exists cycle)
        """

        visited = [0] * 1001

        adjlist = { x: [] for x in range(numCourses)}

        for x,y in prerequisites:
            adjlist[x].append(y)

        def dfs(node):
            if visited[node] == 1:
                return False

            if not adjlist[node] or visited[node] == 2:
                return True
            
            visited[node] = 1   # visiting
            for preq in adjlist[node]:
                if not dfs(preq):
                    return False
            
            visited[node] = 2
            return True
            
        for course in adjlist:
            if not dfs(course):
                return False
                
        return True