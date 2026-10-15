class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        lgt = len(nums)
        def backtrack(i, subset):
            if i == lgt:
                subsets.append(subset.copy())
                return
            
            for n in nums:
                if n not in subset:
                    subset.append(n)
                    backtrack(i+1,subset)
                    subset.pop()

        backtrack(0,[])
        return subsets

