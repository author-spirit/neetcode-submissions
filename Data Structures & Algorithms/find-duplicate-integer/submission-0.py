class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dups = {}
        for n in nums:
            if n in dups:
                return n
            dups[n] = True
        
        return -1
        