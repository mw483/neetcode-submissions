class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # If length of t is longer than s then
        # no substrings would satisfy, so return ""
        if len(t) > len(s):
            return ""
        
        if t == "":
            return ""

        # Dictionary for the characters
        count_t = {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)
        window = {}
        have = 0
        need = len(count_t)

        res = [-1, -1]
        res_len = float("infinity")

        # Minimum size of the window is len(t)
        # Maximum size of the window is len(s)
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in count_t and window[c] == count_t[c]:
                have += 1
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                d = s[l]
                window[d] -= 1
                if d in count_t and window[d] < count_t[d]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if res_len != float("infinity") else ""


