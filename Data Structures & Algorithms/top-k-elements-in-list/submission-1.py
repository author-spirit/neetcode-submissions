class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Group the numbers by its frequency
        # Get the top most K numbers descending order

        import heapq

        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        # How can I bring down to O(nlogn)
        # Sort the frequency by K most times but optimized way
        # Get only in descending order
        # Get the max k items which can perform in O(1) time

        # How can I get the k items?
        # 1. Using reverse sort()
        # 2. Minheap - better
        # 3. Bucketsort 

        # Keep adding until k, then pop
        # min-heap automatically removes lower count

        heap = []
        for i in freq:
            heapq.heappush(heap, (freq[i], i))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        while len(heap) > 0:
            result.append(heapq.heappop(heap)[1])
        
        return result



