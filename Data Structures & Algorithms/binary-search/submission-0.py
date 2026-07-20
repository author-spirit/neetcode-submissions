class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Naive-approach
        # Search in list - linear search
        # Result: O(n) times

        # Better Approach - Binary Search
        # Invariant : The target will always be within left, right range
        # State     : hold left, right and mid indices - in-place (array)
        # Violates  : When the mid number is not the same as target
        # Recover   : If target is lesser than mid then eliminate the mid i.e (mid-1) vice-versa (mid+1) when 
        left, right = 0, len(nums) - 1

        # [-1,0,2,4,6,8], target = 4

        while left <= right:
            mid = (right + left)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        
        return -1


