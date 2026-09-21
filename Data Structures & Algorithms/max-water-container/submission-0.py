class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        max_area = 0

        while p2 > p1:
            max_area = max(max_area, (p2 - p1) * min(heights[p1], heights[p2]))

            if heights[p1] > heights[p2]:
                p2 -= 1
            else:
                p1 += 1
        
        return max_area