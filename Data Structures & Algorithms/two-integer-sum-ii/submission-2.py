class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # naive approach
        # 1. Have two loops, first loop for number selection
        # 2. In second loop, it iterates the rest of numbers 
        #   excluding (first & its before numbers) i+1
        # 3. Sum and compare with the target
        # 4. If it is matched return in 1-indexed way   

        """
        Optimal Approach
        Two Pointers: Array is already sorted
        - Intuition: As the array is sorted, apply the two pointers slowly sequeze till l > r
        - Invariant: Sum of higher number gives higher result
        - Apply left and right pointers on sides of array
        - Compare the sum of two numbers and compare with the target
        - If the sum is greater than target decrement the left, math (sum of larger ~ larger number)
        - If same return [i,j]
        """
        
        l = 0
        r = len(numbers) - 1

        while l < r:
            summ = numbers[l] + numbers[r]
            if summ < target:
                l+=1
            elif summ > target:
                r-=1
            else:
                return [l+1,r+1]
        
        return []









        