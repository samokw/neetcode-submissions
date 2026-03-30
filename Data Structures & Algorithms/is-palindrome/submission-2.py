class Solution:
    def is_alnum(self, c):
        return (ord('a') <= ord(c) <= ord('z') 
        or ord('A') <= ord(c) <= ord('Z') 
        or ord('0') <= ord(c) <= ord('9'))
    def isPalindrome(self, s: str) -> bool:
        
        L, R = 0, len(s) - 1
        
        while L < R:
            # move the l pointer if its not at an alphanumeric character
            while L < R and not self.is_alnum(s[L]):
                L += 1
            
            # move the r pointer if its not at an alphanumeric character
            while L < R and not self.is_alnum(s[R]):
                R -= 1

            # if the character we are currently comparing at the l and r pointer are not the same return false
            if s[L].lower() != s[R].lower():
                return False
            # move the pointers inwards
            L, R = L + 1, R - 1
        
        return True