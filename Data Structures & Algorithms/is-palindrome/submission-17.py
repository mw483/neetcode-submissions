class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not self.isAlphanumeric(s[i]):
                i += 1
            while j > i and not self.isAlphanumeric(s[j]):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i, j = i + 1, j - 1
        return True
    
    def isAlphanumeric(self, c):
            if ord('0') <= ord(c) <= ord('9') or ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z'):
                return True
            else:
                return False 