class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        s - (A-Z0-9), k - characters to replace
        Return the longest substring contains only one distinct character

        how many k(s) can be replaced?
        AAABABB - can't I take full text.

        How long I can prepare for substring?

        Pattern: Variable size sliding window, make use of hashmap to for substring.
        Looks like sliding window but it is more like hashmap

        Naive Approach:
        We count the number of frequencies of each character, then take the highest count
        Then length - len(highest) = remaining different characters count <= k
        if the result of this is less or equal to K then
        replace the other character with the dominated character
        if the difference is more than k then shrink the window & reduce the Lth character
        """

        max_len = 0
        freq = {}
        l = 0
        n = len(s)

        def get_dominate(freq):
            maxx = 0
            for f in freq:
                maxx = max(freq[f], maxx)
            
            return maxx

        # XYYX

        for r in range(n):
            freq[s[r]] = freq.get(s[r], 0) + 1

            dominate = get_dominate(freq)
            diff = (r -l + 1) - dominate 
            if diff > k:
                freq[s[l]] -=1
                l+=1
                continue
                
            max_len = max(max_len, r-l+1) 

        return max_len




            
        