class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        parentheses = ('[','(','{')
        _pop_value = None
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for ch in s:
            if ch in parentheses:
                queue.append(ch)
                continue
            if queue: 
              _pop_value= queue.pop()
            else:
                return False
            if pairs[ch] == _pop_value:    
              continue
            else:
                return False
        return not queue