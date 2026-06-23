class Solution:
    def isHappy(self, n: int) -> bool:
        res = 0
        seen = set()
        while (res != 1):
            digits = [int(d) for d in str(n)] # convert to digits
            for num in digits:
                res += num**2
            if res == 1:
                return True
            if (res in seen):
                return False
            seen.add(res)
            n = res
            res = 0

