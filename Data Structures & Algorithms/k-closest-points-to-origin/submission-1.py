class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # [2,0] <= distance

        # Pattern: Like Priority queue
        # Invariant: The min heap maintain the sorted order
        # state: distance, co-ors, min
        # termination: After distance calculated, return only the k items
        # returns: k times nearest to origin (0,0)
        # Time: O(n + k log(n)), O(n)

        # Max Heap
        # Invariant: Max-heap holds the farthest distance
        # state: items
        # terminate: If len(dis) == k then remove farthest ones 

        dists = []

        import heapq
        for p in points:
            heapq.heappush(dists, [-(p[0]**2 + p[1]**2), p[0], p[1]])

            if len(dists) > k:
                heapq.heappop(dists)

        return [d[1:] for d in dists]

        



