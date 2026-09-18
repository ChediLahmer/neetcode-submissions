class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
      left = []
      stack = []
      right = []
      max_surface = 0
      for idx, element in enumerate(heights):
        while stack and element <= heights[stack[-1]]:
            stack.pop()
        if stack:
            left.append(stack[-1])
        else:
            left.append(-1)
        stack.append(idx)
      stack = []
      for idx, element in reversed(list(enumerate(heights))):
        while stack and element <= heights[stack[-1]]:
            stack.pop()
        if stack:
            right.append(stack[-1])
        else:
            right.append(len(heights))
        surface = heights[idx]*(right[-1] - left[idx]-1)
        if surface > max_surface:
            max_surface = surface
        stack.append(idx)
      return max_surface