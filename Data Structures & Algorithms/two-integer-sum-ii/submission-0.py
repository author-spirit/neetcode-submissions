class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Here numbers are stored in non-descending order
        # numbers can also be in negative
        # Indexing starts from "1"
        # Returns the indices of two sum, where idx1 < idx2
        # Solution => O(1) time

        # naive approach

        for i in range(1,len(numbers)):
            first = numbers[i-1]
            for j in range(i, len(numbers)):
                if first + numbers[j] == target:
                    return [i, j+1]
        
        return []






        