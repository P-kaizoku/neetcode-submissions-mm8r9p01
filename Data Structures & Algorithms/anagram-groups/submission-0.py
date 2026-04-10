class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            x = ''.join(sorted(word))
            if x in anagrams:
                anagrams[x].append(word)
            else:
                anagrams[x] = [word]
        
        ans = [v for v in anagrams.values()]
        return ans

        