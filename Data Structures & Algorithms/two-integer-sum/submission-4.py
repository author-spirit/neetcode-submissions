class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute-force: Take a number and add and compare the next list of numbers with target
        
        # Better: Store the differences by subtracting number with target in hashmap
        # Iterate all the numbers and check if the number existing in the hashmap
        # Get the index of difference number found, where i != j
        # If found then return [i,j]

        # compliments = {}
        # for i,n in enumerate(nums):
        #     diff = target - n
        #     compliments[diff] = i

        # for n in compliments:
        #     diff = target - n
        #     if diff in compliments and compliments[n] != compliments[diff]:
        #         return [compliments[n], compliments[diff]]
        
        # return []

        # store all the compliments in hashmap
        # 

        compliments = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in compliments:
                return [compliments[diff], i]
            
            compliments[num] = i
        
        return []
