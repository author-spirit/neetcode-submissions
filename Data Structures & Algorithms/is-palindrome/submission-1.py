class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Naive approach
        # remove all non-alpha numeric and compare

        new_str = ""
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        
        print(new_str)
        return new_str[:] == new_str[::-1]
        