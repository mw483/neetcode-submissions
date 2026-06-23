class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = "" # Declare empty string
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string  

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0 # Initialize string pointer

        while i < len(s):
            j = i
            while s[j] != "#": # Loop through characters while not # to read the digit
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length                
            strs.append(s[i:j]) 
            i = j

        return strs

