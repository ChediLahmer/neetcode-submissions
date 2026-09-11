class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        for ch in s:
            if ch == '[':
                queue.append(']')
            elif ch == '(':
                queue.append(')')
            elif ch == '{':
                queue.append('}')
            else:
              if not queue or queue.pop() !=ch:
                return False
        return not queue