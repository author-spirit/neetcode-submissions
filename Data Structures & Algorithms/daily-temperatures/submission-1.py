class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Temperature -> Daily temperature
        # result -> If no warmer in future set 0

        # Brute force
        # Check each temperature and its next first warmer temperature (else 0)
        # Deciding warmer day: If current temp is more than.
        # Time: O(n^2)

        # Better approach
        # Invariant: warmer temperature appears after the cooler days
        # state: remember the warmer day
        # violates: when no warmer temperature, when all temperature of same
        # recovers: skip the current day and check the next day future temperature

        # [30,38,30,36,35,40,28]

        warmer = []

        days = len(temperatures) - 1
        result = [0] * len(temperatures)

        while days >= 0:
            if not warmer:
                warmer.append(days)
            else:
                while len(warmer) and temperatures[days] >= temperatures[warmer[-1]]:
                    warmer.pop()
                
                if len(warmer):
                    result[days] = warmer[-1] - days
                warmer.append(days)

            days -=1
        
        return result


        