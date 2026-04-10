class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp1 = Counter(s1)
        k = len(s1)
        mp2 = Counter(s2[:k])

        if mp1 == mp2: return True
        for i in range(k, len(s2)):
            mp2[s2[i]] = mp2.get(s2[i], 0) +1
        
            mp2[s2[i-k]] -= 1
            if mp2[s2[i-k]] == 0:
                del mp2[s2[i-k]]
            
            if mp1 == mp2: return True
        return False
                    