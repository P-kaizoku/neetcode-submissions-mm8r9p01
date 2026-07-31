class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str not in result:
                result[sorted_str] = [s]
                continue
            result[sorted_str].append(s)
        
        return [x for x in result.values()]