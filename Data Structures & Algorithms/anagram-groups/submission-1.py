class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # You take the characters and its occurences
        # Do the same for next string, character : occurence
        # {"e": 1, "a": 1, "t": 1}
        # An anagram strings must of same size

        # Brute-force: Get the character : occurences of all strings of 
        # same size and compare, ignore already grouped ones
        # visible edge-cases: can have difference sizes

        # Better solution
        # Bring down the O(n^2) -> O(n)
        # Can I fast compare the two strings -> But car, cat are anagrams
        # I need to have unique identifier
        # Do? char: freq required? - Give accuracy
        # Do? holding prev ones resolves this?

        results = {}
        for anagram in strs:
            sorted_str = "".join(sorted([c for c in anagram]))
            if sorted_str in results:
                results[sorted_str].append(anagram)
            else:
                results[sorted_str] = [anagram] 

        return list(results.values())