class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # You take the characters and its occurences
        # Do the same for next string, character : occurence
        # {"e": 1, "a": 1, "t": 1}
        # An anagram strings must of same size

        # Brute-force: Get the character : occurences of all strings of same size
        # visible edge-cases: can have difference sizes

        result = []
        anagrams = []

        for _str in strs:
            anagram = {"occurences": {}, "str": _str}
            for c in _str:
                anagram['occurences'][c] = anagram['occurences'].get(c, 0) + 1
            anagram["str"] = _str
            anagrams.append(anagram)
        
        ignore = set()
        for i in range(len(anagrams)):
            if i in ignore:
                continue
            first = anagrams[i]['occurences']
            groups = [anagrams[i]['str']]
            for j in range(i+1, len(anagrams)):
                if j in ignore:
                    continue
                if first == anagrams[j]['occurences']:
                    groups.append(anagrams[j]['str'])
                    ignore.add(i)
                    ignore.add(j)
            
            result.append(groups)
        
        return result