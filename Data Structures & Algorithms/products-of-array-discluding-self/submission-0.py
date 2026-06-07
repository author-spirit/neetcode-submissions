class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Return the product of all nums in array except the self number

        # Brute-force: We iterate through all the nums
        # we gonna have another loop that multiples all the nums excluding the parent num
        # push the multiplied numbers to output array
        # This results in O(n^2) time operation, O(n) space - result

        output = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                prod *=nums[j]

            output.append(prod)
        
        return output
    