class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Invariant: The substring holds non-duplicate characters seen so far
        # state: substring hash, L & R
        # terminate: when new character found in substring then calculate the substring length and update L
        # pattern: sliding window
        # time: O(1). space = O(n)

        charset = set()
        length = 0

        l = 0
        r = 0

        while r < len(s):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1

            charset.add(s[r])
            length = max(length, len(charset))
            r+=1

        return length

        