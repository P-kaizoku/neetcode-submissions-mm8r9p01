class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mp = defaultdict(int)

        for i, j in zip(s, t):
            mp[i] += 1
            mp[j] -= 1
        
        for value in mp.values():
            if value != 0:
                return False
        
        return True