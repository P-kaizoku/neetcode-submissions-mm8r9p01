class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for word in strs:
            x = "".join(sorted(word))
            mp[x].append(word)
        
        return list(mp.values())