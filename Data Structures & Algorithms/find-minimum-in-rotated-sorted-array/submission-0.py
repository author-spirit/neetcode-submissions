class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1,2,3,4,5,6 -> 4times -> 3,4,5,6,1,2
        
        # Naive-approach
        # Find the number in the array, but cannot scale for larger list

        # better approach
        # binary search
        # 1st and last 3>2[✓], 4>2[✓], 5>2[✓], 6>2[✓], 1>2[x] = total is 4

        if not nums:
            return 0
        
        l = 0
        r = len(nums)-1
        times = 0

        while nums[l] > nums[r]:
            print(l)
            times+=1
            l+=1
    
        return nums[l]
