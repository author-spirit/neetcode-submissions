class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Invariant: The starting num of a sequence is 
        #           considered if (num - 1) is not available in array
        # state: list_set, longest sequence
        # terminate: when num + 1 not in set then update the longest
        # pattern: set boundary

        listset = set(nums)

        long_seq = 0

        for num in listset:
            # start of seqeunce
            if num - 1 not in listset:
                length = 1

                # exactly 1 greater than the previous element
                # time complexity, is not affected. O(n+n) = O(n)
                # because no starting numbers are skipped 
                while num + length in listset:
                    length +=1
                long_seq = max(length, long_seq)

        return long_seq
            
            


        




            