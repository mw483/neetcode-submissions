class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = "" # Declare empty string
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string  

    def decode(self, s: str) -> List[str]:
        strs = []

        i = 0 # Initialize string pointer
        str_len = ""

        while i < len(s):
            while s[i] != "#": # Loop through characters while not # to read the digit
                str_len += s[i]
                i += 1                
            strs.append(s[i+1:i+1+int(str_len)]) 
            i += int(str_len) + 1
            str_len = ""

        return strs

