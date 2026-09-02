class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        for letter in s:
            t_count = t.count(letter)
            s_count = s.count(letter)
            if s_count != t_count:
                return False
        return True