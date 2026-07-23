class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1,2,3,4,5,6 -> 4times -> 3,4,5,6,1,2
        
        """
        Naive-approach:
            Find the number in the array
            Keep checking the numbers in the list with last number
            Why because if it rotated then last number may hold the lower number
            if 1st number is greater than last number then check next numbers
            stop when number is lesser than last number, then return the lower number by index
        Time: O(n)
        """

        """
        Better Approach
        Invariant: The lowest appears before the highest number
        State: Binary Search
        Violates: when highest number appears before the lower number
        Restore: Consider the violated block
        Edge Case: the numbers are between 1 to N, finding the lowest is easy.
                    just get the diff between N - last_index_value
        Time:O(logn)
        """

        
        # [-3,-2,-1,0,1,2] -3 2 -1/2
        # [-1,0,1,2,-3,-2] 6+2
        # [3,4,5,1,2]

        left = 0
        right = len(nums)-1
        mid = 0
        
        while left < right:
            mid = (left + right)//2

            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid

        return nums[left]
            















