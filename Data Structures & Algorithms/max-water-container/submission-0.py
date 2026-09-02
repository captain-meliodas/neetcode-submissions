class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        max_area = 0
        while l<r:
            l_height,r_height = heights[l], heights[r]
            curr_area = min(l_height,r_height) * (r-l)
            max_area = max(max_area, curr_area)
            if l_height < r_height:
                l += 1
                while l<r and l_height >= heights[l]:
                    l += 1
            else:
                r -= 1
                while l<r and r_height >= heights[r]:
                    r -= 1
        
        return max_area
        