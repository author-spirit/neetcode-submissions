class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Return the product of all nums in array except the self number

        # Brute-force: We iterate through all the nums
        # we gonna have another loop that multiples all the nums excluding the parent num
        # push the multiplied numbers to output array
        # This results in O(n^2) time operation, O(n) space - result

        # Better approach - follow-up
        # ---
        # Instead of computing the product multiple times keep track of product
        # With division: I just take product of all nums, then divide product with each num
        # But division method is not allowed

        # Efficient solution - without division 
        # How can you skip the current number from product?   
        # Loop nums, take last number and multiple 0 -> n-1, 1 -> n-2
        # Hidden: Someone or state completely ignores current number from product
        # Can I split into two arrays [..] cur [...]
        
        def product(arr):
            result = 1
            for i in arr:
                result *=i
            return result


        output = []
        for i in range(len(nums)):
            res1 = 1
            res2 = 1

            # If last index 3
            # 0:3, 3+1:  -> 4 fails
            # index=2
            # 0:2, 2+1   -> i+1 < n

            if i !=0:
                res1 = product(nums[0:i])
            if i+1 < len(nums):
                res2 = product(nums[i+1:])

            print(res1, res2)
            output.append(res1 * res2)

        return output
        
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                prod *=nums[j]

            output.append(prod)
        
        return output
    