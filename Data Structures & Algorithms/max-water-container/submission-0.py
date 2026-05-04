class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        l = 0
        r = len(heights) - 1
        while l <= r:
            contained = min(heights[r],heights[l])*(r-l)
            best = max(best,contained)
            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        return best