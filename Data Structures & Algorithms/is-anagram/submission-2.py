class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sol1: sort the characters and compare the string
        # return sorted([i for i in t]) ==  sorted([i for i in s]) 

        # Sol2: add first string to hashmap and keep the frequency
        # Sol3: Have a fixed length array, if character of first string increments then 2nd string decrements
        #       On further scan if there exist non-zero pos-ve count then either one has missing/different character.

        if len(s) != len(t):
            return False

        alpha = [0] * 26

        for a in range(len(s)):
            char_pos_s = ord(s[a]) - 97
            char_pos_t = ord(t[a]) - 97
            alpha[char_pos_s]+=1
            alpha[char_pos_t]-=1

        print(alpha)
            
        for a in alpha:
            if a != 0:
                return False
        
        return True
        
        