class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most  = 0
        left = 0
        right = len(heights) -1
        while left < right:
            dif = right - left
            area = dif * min(heights[left], heights[right])
            most = max(most, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return most
        