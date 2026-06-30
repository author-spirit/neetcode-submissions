class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Sol: Find longest substring
        # 1. without duplicate characters - consecutive
        # 2. s - printable ASCII chars (space, num, upper, lower, symbols)

        # Naive approach
        # - zxyzxyz
        # Track the contiguous substring
        # Let have two loops, first loop starts the character
        # And second loop track the substring
        # But tracking must stop duplicate character
        # Once duplicate found track the the length of of substring
        # To track the duplicate let's use set or hashmap
        # Let's have max_length

        # zxyzxyz

        max_len = 0
        for i in range(len(s)):
            subs = ""
            dups = set()
            for j in range(i, len(s)):
                if s[j] in dups:
                    break
                
                print(subs)

                subs += s[j]
                dups.add(s[j])
                max_len = max(max_len, len(subs))
            
        return max_len

        



        