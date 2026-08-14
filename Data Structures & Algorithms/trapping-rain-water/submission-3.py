class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)

        lmax = [0 for _ in range(n)]
        rmax = [0 for _ in range(n)]

        lmax[0] = height[0]

        for i in range(1, n):
            lmax[i] = max(height[i], lmax[i-1])

        rmax[-1] = height[-1]

        for i in range(n-2, -1, -1):
            rmax[i] = max(height[i], rmax[i+1])
        

        water = 0

        for i in range(n):
            water += min(lmax[i], rmax[i]) - height[i]
        
        return water