class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False

        count = dict()
        for i in range(len(s)):
            letter_s = s[i]
            letter_r = t[i]
            c_s = count.get(letter_s,0)
            count.update({letter_s : c_s+1 })
            c_r = count.get(letter_r,0)
            count.update({letter_r : c_r-1})
        return all(0==value for value in count.values())