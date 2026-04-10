import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowk = 1
        highk = max(piles)
        

        while lowk<highk:
            midk = lowk + (highk-lowk)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/midk)
            
            if hours <= h:
                highk = midk
            else:
                lowk = midk + 1
        
        return lowk