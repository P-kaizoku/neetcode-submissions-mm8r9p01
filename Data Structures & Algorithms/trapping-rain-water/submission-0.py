class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        prefix_sum = [0]*n
        suffix_sum = [0]*n

        prefix_sum[0] = height[0]

        for i in range(1, n):
            prefix_sum[i] = max(prefix_sum[i-1], height[i])

        suffix_sum[n-1] = height[n-1]

        for i in range(n-2, -1, -1):
            suffix_sum[i] = max(suffix_sum[i+1], height[i])

        total = 0
        for i in range(n):
            leftMax = prefix_sum[i]
            rightMax = suffix_sum[i]

            if (height[i]<leftMax and height[i]<rightMax):
                water = min(leftMax, rightMax) - height[i]
                total += water
        
        return total
