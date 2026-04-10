class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = height[0]
        rightMax = height[n-1]
        total = 0
        i = 0
        j = n-1

        while (i<j):
            if (height[i]<=height[j]):
                if (height[i]<leftMax):
                    water = leftMax - height[i]
                    total += water
                i+=1
            else:
                if (height[j]<rightMax):
                    water = rightMax - height[j]
                    total += water
                j-=1
            
            leftMax = max(height[i], leftMax)
            rightMax = max(height[j], rightMax)

        return total
            