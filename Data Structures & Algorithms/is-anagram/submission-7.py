class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        mp = defaultdict(int)

        for i, j in zip(s,t):
            mp[i] += 1
            mp[j] -= 1
        

        for v in mp.values():
            if v != 0:
                return False
        
        return True