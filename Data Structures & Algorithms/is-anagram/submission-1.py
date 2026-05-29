class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sol1: sort the characters and compare the string
        # return sorted([i for i in t]) ==  sorted([i for i in s]) 

        # Sol2: add first string to hashmap and keep the frequency
        

        freq_s = {}
        freq_t = {}
        
        for c in s:
            freq_s[c] = freq_s.get(c, 0) + 1

        for c in t:
            freq_t[c] = freq_t.get(c, 0) + 1
        
         
        return freq_s == freq_t
        
        