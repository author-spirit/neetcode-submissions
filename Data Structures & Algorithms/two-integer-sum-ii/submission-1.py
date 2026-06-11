class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Here numbers are stored in non-descending order
        # numbers can also be in negative
        # Indexing starts from "1"
        # Returns the indices of two sum, where idx1 < idx2
        # Solution => O(1) time

        # naive approach
        # 1. Have two loops, first loop for number selection
        # 2. In second loop, it iterates the rest of numbers 
        #   excluding (first & its before numbers) i+1
        # 3. Sum and compare with the target
        # 4. If it is matched return in 1-indexed way   

        """
        Better approach:
        1. Is it sorted?
        2. You must use O(1) additional space
        3. Index1 < index2

        Solution:
        1. Have hashmap to store the compliments
        2. On diff with target - cur_num = diff is in compliment
            Then compare whether the comp_index > the cur_index
            If YES, return in 1-indexed
            else, store the cur_num: cur_idx
        """

        compliments = {}

        for i, num in enumerate(numbers):
            diff = target - num
            if diff in compliments and compliments[diff] != i:
                if compliments[diff] < i:
                    return [compliments[diff]+1, i+1]

                return [i+1, compliments[diff]+1]
            
            compliments[num] = i
        
        return []









        