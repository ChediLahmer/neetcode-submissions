class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        for letter in s:
            idx = t.find(letter)
            if idx < 0:
                return False
            t= t.replace(t[idx],"",1)
        if len(t)!=0:
            return False
        return True