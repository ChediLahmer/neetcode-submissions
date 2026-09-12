class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        result = [0] * len(temperatures)
        for idx in range(len(temperatures)-1, -1, -1):
            while stack and temperatures[idx] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                result[idx] = stack[-1] - idx
            stack.append(idx)
        return result