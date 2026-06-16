class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # Statement: Return the 2 bar that holds more water.

        # doubts: If I sort this can it get distorted?
        # This is more like in-place check.

        # invariants
        
        max_area = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            max_area = max(area, max_area)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        
        return max_area