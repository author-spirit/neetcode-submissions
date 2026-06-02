class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Group the numbers by its frequency
        # Get the top most K numbers descending order

        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        items = list(freq.items())
        items.sort(key=lambda key: key[1], reverse=True)

        result = []
        for i in range(k):
            result.append(items[i][0])
        
        return result

        