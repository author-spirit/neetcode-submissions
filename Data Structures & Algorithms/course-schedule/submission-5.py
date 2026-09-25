class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Invariant: A course pre-requisite must complete first
        # Remember: Result, taken {bool = taken/not yet}
        # terminate: if course is already taken then skip and shift to another course

        self.taken = [0]*numCourses
        self.adj = [[] for _ in range(numCourses)]


        for adj in prerequisites:
            a, b = adj
            self.adj[a].append(b)

        # [[1], []]

        def dfs(i):
            if self.taken[i] == 1:
                return False
            
            if self.adj == []:
                return True
            
            self.taken[i] = 1
            for p in self.adj[i]:
                if not dfs(p):
                    return False
            
            self.taken[i] = 2
            self.adj[i] = []
            
            return True

        for c in range(numCourses):
            if dfs(c) == 0:
                return False
        
        return True