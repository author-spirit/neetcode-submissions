class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Naive approach
        # remove all non-alpha numeric and compare

        # abba -> L & R
        # odd -> LR
        # even -> abbA 
        # odd -> eCe

        # invariant: LR must be always same chars and same length
        # eliminate all non-alphanums

        new_str = ""
        for c in s:
            if c.isalnum():
                new_str += c.lower()

        l = 0
        r = len(new_str) - 1
        print(new_str)
        while l < r:
            print(l, r)
            if new_str[l] != new_str[r]:
                return False
            
            l +=1
            r -=1
        
        return True

        