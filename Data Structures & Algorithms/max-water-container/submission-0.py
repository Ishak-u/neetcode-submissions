class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        max_area=0
        while left<right:
            left_h=heights[left]
            right_h=heights[right]
            width=right-left
            current_area=min(left_h,right_h)*width
            max_area=max(current_area,max_area)
            if left_h<right_h:
                left+=1
            else:
                right-=1
        return max_area