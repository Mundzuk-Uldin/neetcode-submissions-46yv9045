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
                # Invalid answer
                l = m +1
            else:
                # Best solution but find if there's a better one
                best = m
                r = m-1
        return best
    
    def canEatBananas(self, piles, k, h, best):
        count = 0
        for x in piles:
            count += math.ceil(x/k)
        if count > h:
            # Invalid Answer
            return -1
        return 0
        