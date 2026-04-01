import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        best = r
        while l <= r:
            m = (l + r)//2
            i = self.canEatBananas(piles, m, h, best)
            if i < 0:
                l = m +1
            elif i > 0:
                r = m-1
            else:
                best = m
                r = m-1
        return best
    
    def canEatBananas(self, piles, k, h, best):
        count = 0
        for x in piles:
            count += math.ceil(x/k)
        if count > h:
            return -1
        # There's a better solution
        if k > best:
            return 1
        # Best solution
        return 0
        