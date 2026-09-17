class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Invariant: Traverse on adjacent 1's form an island
        # state: visited, count
        # violation: if no adjacent 1s found
        # recover: loop through unvisited 1's and start from it.
        if not grid or not grid[0]:
            return 0

        self.visited = {}
        count = 0

        def dfs(i,j,grid):
            if not ((i >=0 and i < len(grid)) and (j >= 0 and j < len(grid[0]))):
                return 

            if (i,j) in self.visited:
                return
            
            if grid[i][j] == "0":
                return

            self.visited[(i,j)] = True
            for node in ((0,-1), (0,1), (-1,0), (1,0)):
                x = i + node[0]
                y = j + node[1]
                if (x,y) not in self.visited:
                    dfs(x, y, grid)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue

                if (i,j) in self.visited:
                    continue
                print("i,j", (i,j))
                
                count +=1
                dfs(i,j,grid)

        return count


                
