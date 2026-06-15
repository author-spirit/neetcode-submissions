class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()

        # sorted: [-4, -1, -1, 0, 1, 2]

        triplets = []

        n = len(nums) - 1

        for i, first in enumerate(nums):

            l = i+1
            r = n

            # allow it run once
            if i > 0 and nums[i-1] == nums[i]:
                continue

            while l < r:
                summ = first + nums[l] + nums[r]

                if summ == 0:
                    triplets.append([first, nums[l], nums[r]])
                    l+=1
                    while nums[l-1] == nums[l] and l < r:
                        l+=1
                elif summ > 0:
                    r-=1
                else:
                    l+=1
                    while nums[l-1] == nums[l] and l < r:
                        l+=1

        return triplets