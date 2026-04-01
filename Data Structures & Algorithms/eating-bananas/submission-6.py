import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        best = r
        while l <= r:
            m = (l + r)//2
            if self.canEatBananas(piles, m, h, best) == -1:
                l = m +1
            else:
                best = m
                r = m-1
        return best
    
    def canEatBananas(self, piles, k, h, best):
        count = 0
        for x in piles:
            count += math.ceil(x/k)
        if count <= h and k <= best:
            return 0
        if count > h:
            return -1