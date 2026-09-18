class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)

        for idx in range(n + 1):
            current_height = 0 if idx == n else heights[idx]

            while stack and (
                idx == n or heights[stack[-1]] >= current_height
            ):
                popped_idx = stack.pop()
                height = heights[popped_idx]

                left_boundary = stack[-1] if stack else -1
                width = idx - left_boundary - 1
                area = height * width

                max_area = max(max_area, area)

            if idx < n:
                stack.append(idx)

        return max_area