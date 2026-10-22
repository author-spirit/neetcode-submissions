class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Invariant: Max heap maintains the result of first two numbers
        # state: max-heap
        # termination: 
        #   if len(x) == 1 -> return stones[0]
        #   if x == y => both re destroyed so no new
        #   if x < y => push(y-x)
        #   if y < x => push(x-y)

        import heapq

        stonez = [-s for s in stones]

        heapq.heapify(stonez)
        print(stonez)

        while len(stonez) > 1:
            x = -heapq.heappop(stonez)
            y = -heapq.heappop(stonez)

            if x < y:
                heapq.heappush(stonez, -(y-x))
            elif y < x:
                heapq.heappush(stonez, -(x-y))
            
        return -stonez[0] if stonez else 0
            