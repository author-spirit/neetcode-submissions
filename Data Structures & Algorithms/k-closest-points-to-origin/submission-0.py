class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # [2,0] <= distance

        # Invariant: The min heap maintain the n nearest points - 0
        # state: distance, co-ors, min
        # termination: After distance calculated, if k == 0 then stop adding to list
        # returns: k times nearest to origin (0,0)

        # Pattern: Priority queue

        dists = []

        for p in points:
            dists.append([(p[0]**2 + p[1]**2), p[0], p[1]])

        import heapq

        heapq.heapify(dists)

        print(dists)

        items = []

        # 4,4,8 

        i = 0
        while i < k:
            dis, x, y = heapq.heappop(dists)
            items.append([x,y])
            i +=1
        
        return items

        



