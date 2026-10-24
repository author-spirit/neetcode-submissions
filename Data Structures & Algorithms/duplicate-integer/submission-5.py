class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # The best solution would be store the numbers in HashSet
        # We just have to check if number is already in hashset
        # No need of counting, just one entry can say the number exists

        return len(list(set(nums))) != len(nums)

        