class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        res = 0

        # loop through available characters in charSet
        for c in charSet:
        # for each character, set left pointer and count to 0
            l = count = 0
        # loop through the string with the right pointer
            for r in range(len(s)):
                # add the count if the right pointer equals the current char
                if s[r] == c:
                    count += 1
                # while more than the available number of replacements need to be made, reduce the sliding window size
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                
                # update max
                res = max(res, r - l + 1)
        return res

        
