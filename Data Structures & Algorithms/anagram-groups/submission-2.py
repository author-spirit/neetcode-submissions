class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Invariant: Group the character frequencies will give anagrams
        # state: anagrams - hashmap, group
        # execution: if the character frequency not in anagram then group them new

        anagrams = {}
        for word in strs:
            counts = [0]*26
            for c in word:
                code = ord(c) - 97
                counts[code]+=1
            
            anagram = tuple(counts)
            if anagram in anagrams:
                anagrams[anagram].append(word)
            else:
                anagrams[anagram] = [word]
            
        return list(anagrams.values())