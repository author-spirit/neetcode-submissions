class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Better approach
        # Sliding window: To get the longest substring without duplicates
        # To determine whether character is duplicate we use the hashmap
        # to store the character and its last seen index
        # Here we use two pointers - L & R, here Right completes fully
        # The length of of L gets shrinked when R sees duplicate character
        # So the L position is moved forward by the duplicate character's previous last_seen
        # The L pos is shifted one step ahead of last seen position, if L
        # Calculate the length between L & R and update the max_length

        # The problem looks like sliding window, but it uses hashmap and 2 pointers

        # Invariant: all characters are unique, r moves always first
        # Becareful: L shifting, it should always shrink, the duplicate character's last_seen
        # should be more than the current L position else this can open up bugs (wrong substring)

        max_length = 0
        l = 0
        dups = {}

        # abba

        for r in range(len(s)):
            if s[r] in dups:
                if dups[s[r]] >= l: # l = 2, dup = 1
                    l = dups[s[r]] + 1

            max_length = max(max_length, r-l+1)
            dups[s[r]] = r

        return max_length 
