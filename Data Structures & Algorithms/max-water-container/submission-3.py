class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1

        maxVol = 0
        while l < r:
            height = min(heights[l], heights[r])
            width = r-l

            maxVol = max(maxVol, height*width)

            if heights[l]<heights[r]:
                curr=l
                for i in range(curr, r):
                    if heights[i] > heights[curr]:
                        l = i
                        break
                if curr == l:
                    break
            else:
                curr = r
                for i in range(curr, -1, -1):
                    if heights[i] > heights[curr]:
                        r = i
                        break
                if curr == r:
                    break

        
        return maxVol
