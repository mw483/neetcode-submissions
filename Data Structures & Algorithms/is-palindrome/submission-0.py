class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        # Filter non-alphanumeric
        cleaned_s = "".join([c for c in s if c.isalnum()]).upper()
        for i, c in enumerate(cleaned_s):
            j = len(cleaned_s) - 1 - i
            if cleaned_s[i] != cleaned_s[j]:
                return False
        return True
