class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        # Initialize second pointer
        j = len(s) - 1
        while i < j:
            # Skip if not lower case alphabet
            while i < j and not self.alphaNum(s[i]):
                i += 1
            # Skip if not lower case alphabet
            while i < j and not self.alphaNum(s[j]):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i = i + 1
            j = j - 1
        return True    
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
