class Solution:
    def isPalindrome(self, s: str) -> bool:
        is_palindrome = True
        s= ''.join(filter(str.isalnum, s))
        s= s.lower()
        j = len(s)-1
        i = 0
        while i!=j and i<j and is_palindrome:
            if s[i] != s[j]:
                is_palindrome=False
            i+=1
            j-=1

        return is_palindrome