class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights) # How many heights we have

        l = 0
        r = n - 1
        max_area = 0

        while l < r:    # not <= since we dont want to process the same bar

            w = r - l                       # Width is difference from right - left indicies
            h = min(heights[l], heights[r])   # choose smaller height to properly get the area
            a = w * h                       # area = width x height
            max_area = max(max_area, a)     # choose the max area btwn what it was before or the one in this curr iteration

            if ( heights[l] < heights[r] ):
                l += 1
            else: 
                r -= 1

        return max_area



        