class Solution:
    def isHappy(self, n: int) -> bool:

        # invariant: Diving N by 10 gives each remainder i.e each digit
        # state: digit, rem, sum
        # terminate: When the result becomes zero
        
        # 100/10 -> 10 -> 0
        # 10/10 -> 1 > 0
        # 1/10 -> int(0.1) -> 1

        def get_sum(n):
            sum = 0
            digit = n
            rem = 0

            while digit > 0:
                rem = digit % 10
                digit = digit // 10

                sum += rem**2

            return sum

        seen = set()
        sum = get_sum(n)
        seen.add(sum)
        while sum != 1:
            sum = get_sum(sum)
            if sum in seen:
                return False
            
            seen.add(sum)
            
        return True


