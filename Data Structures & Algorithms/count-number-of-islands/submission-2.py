class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Invariant: Traverse on adjacent 1's form an island
        # state: visited, count, adjacents (4)
        # violation: if no adjacent 1s found
        # recover: loop through unvisited 1's and start from it.
        

        if not grid or not grid[0]:
            return 0
        
        count = 0
        self.visited = set()
        self.adjacents = ((0,-1), (0,1), (-1,0), (1,0))

        def adjacency(adj):
            x,y = adj
            if adj in self.visited or grid[x][y] == "0":
                return

            print(adj)

            self.visited.add(adj)
            for adj_x, adj_y in self.adjacents:
                newx = x + adj_x
                newy = y + adj_y
                if (newx >= 0 and newx < len(grid)) and (newy >= 0 and newy < len(grid[0])):
                    adjacency((newx, newy))
            
            return

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (x, y) in self.visited or grid[x][y] == "0":
                    continue

                print("new")

                adjacency((x,y))
                count += 1

        return count



                
