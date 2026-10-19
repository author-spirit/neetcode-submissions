import heapq

class KthLargest:

    def balance(self):

        while len(self.stream) > self.k:
            heapq.heappop(self.stream)

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = nums
        heapq.heapify(self.stream)
        self.balance()

    def add(self, val: int) -> int:
        
        heapq.heappush(self.stream, val)
        self.balance()
        return self.stream[0]
    
        
