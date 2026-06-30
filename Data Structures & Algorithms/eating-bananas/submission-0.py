class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # my guess: binary search based on the minimum and maximum eating rate.
        # in binary search we have to find the "target"
        # the target in this case is the minimum eating rate.
        # how do we define the minimum eating rate based on the available numbers.
        # for piles = [1,4,3,2] there is no point going more than 4 bananas per second.
        # so, the upper bound is the pile with the most bananas.
        # things to consider: # of piles
        # if there are h hours and p piles then we have to finish each pile in an average of h/p hours/pile
        # in the case of [1,4,3,2] with h=9
        r = max(piles)
        l = 1
        res = r

        while l <= r:
            k = (l + r) // 2
            time = 0
            for p in piles:
                time += math.ceil(float(p) / k)
            # if using the current speed, the time is less than or equal to h, we can reduce the speed
            if time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res


                



