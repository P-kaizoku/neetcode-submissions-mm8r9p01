class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)

        for i in range(n):
            current_height = heights[i]


            left = i
            while left > 0 and heights[left-1] >= current_height:
                left -= 1
            

            right = i
            while right < n-1 and heights[right+1] >= current_height:
                right += 1
            
            width = right - left + 1

            max_area = max(max_area, current_height*width)
        
        return max_area