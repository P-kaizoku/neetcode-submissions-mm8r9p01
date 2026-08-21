class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canEat(k):
            eta = 0

            for x in piles:
                eta += math.ceil(x/k)
            
            return eta <= h
        

        n = max(piles)

        l, r = 1, n

        bestEta = n
        while l <= r:
            m = r - (r-l)//2

            if canEat(m):
                bestEta = min(bestEta, m)
                r = m-1
            else:
                l = m+1
        
        return bestEta
               