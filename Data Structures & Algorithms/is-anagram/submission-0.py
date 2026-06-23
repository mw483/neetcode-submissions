class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = {}
        t_letters = {}
        for char in s:
            s_letters[char] = s_letters.get(char, 0) + 1
        for char in t:
            t_letters[char] = t_letters.get(char, 0) + 1
        if s_letters == t_letters:
            return True
        else:
            return False
