class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        parentheses = ('[','(','{')
        _pop_value = None
        for ch in s:
            if ch in parentheses:
                queue.append(ch)
                continue
            if queue: 
              _pop_value= queue.pop()
            else:
                return False
            if (ch == ']' and _pop_value == '[') or (ch == ')' and _pop_value == '(') or (ch == '}' and _pop_value == '{'):    
              continue
            else:
                return False
        if not queue:
            return True
        else: 
            return False