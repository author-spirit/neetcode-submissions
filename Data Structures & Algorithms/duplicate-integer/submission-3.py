class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # store in one medium to get the frequency counts
        # we can have an array exlcuding the 0th index, and use rest
        # this is exist to resolve the repeat numbers, 
        # one catch is it can also accept neg've numbers
        # so this looks like frequency count but twist is neg-ve
        # sort and keep previous number
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        
        # return False

        # repeat = float('inf')
        # nums.sort()
        # for i in nums:
        #     if repeat == i:
        #         return True
        #     else:
        #         repeat = i
        
        # return False

        # keep track of numbers in a hashmap, because this can perform at O(1) time
        # and easy to check the number if the count is more than 1 and no need to sort

        repeats = {}
        for n in nums:
            if repeats.get(n, 0) > 0:
                return True

            repeats[n] = repeats.get(n, 0) + 1
        
        return False

        