class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0 for i in range(len(height))]
        currMax = height[0]
        for i in range(1,len(height)):
            prefix[i] = currMax
            currMax = max(currMax, height[i])
        suffix = [0 for i in range(len(height))]
        currMax = height[-1]
        for i in range(len(height)-2,0,-1):
            suffix[i] = currMax
            currMax = max(currMax, height[i])
        total = 0
        for i in range(len(height)):
            total += max(min(prefix[i],suffix[i])-height[i],0)
        return total