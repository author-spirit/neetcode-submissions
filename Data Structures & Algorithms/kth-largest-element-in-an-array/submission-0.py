class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Invariant: The largest numbers appears top
        # state: values in max-heap - so largest number first
        # terminate: stop at k

        import heapq
        values = []

        for num in nums:
            heapq.heappush(values, -num)

        for i in range(len(nums)):
            val = -heapq.heappop(values)
            if i+1==k:
                return val

        return 0 
        