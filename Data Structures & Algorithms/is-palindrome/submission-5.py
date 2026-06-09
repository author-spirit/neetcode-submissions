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

        l = 0
        r = len(s) - 1
        while l < r and l < len(s) and r >= 0:
            print(s[l], s[r])

            if not s[l].isalnum():
                l +=1
                continue
            
            if not s[r].isalnum():
                r -=1
                continue

            if s[l].lower() != s[r].lower():
                return False
            
            l +=1
            r -=1
        
        return True

        